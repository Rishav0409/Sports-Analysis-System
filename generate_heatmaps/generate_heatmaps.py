import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Paths
video_path = "../Input_Videos/08fd33_4.mp4"
output_folder = "output_heatmaps"
os.makedirs(output_folder, exist_ok=True)

# Initialize storage for positions
team_a_positions = []
team_b_positions = []

# Load video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # TODO: Replace the following with real tracking logic
    # Mock example: randomly generate player positions
    for _ in range(11):
        team_a_positions.append((np.random.randint(0, frame.shape[1]), np.random.randint(0, frame.shape[0])))
        team_b_positions.append((np.random.randint(0, frame.shape[1]), np.random.randint(0, frame.shape[0])))

cap.release()

# Convert to numpy arrays
team_a_np = np.array(team_a_positions)
team_b_np = np.array(team_b_positions)

# Create and save heatmaps
def plot_heatmap(positions, title, filename):
    if positions.size == 0:
        print(f"No data to plot for {title}")
        return
    x, y = positions[:, 0], positions[:, 1]
    plt.figure(figsize=(10, 6))
    sns.kdeplot(x=x, y=y, cmap="Reds", fill=True, bw_adjust=0.3, thresh=0.01)
    plt.title(title)
    plt.xlim(0, 1280)
    plt.ylim(720, 0)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig(os.path.join(output_folder, filename))
    plt.close()

plot_heatmap(team_a_np, "Team A Heatmap", "team_a_heatmap.png")
plot_heatmap(team_b_np, "Team B Heatmap", "team_b_heatmap.png")

print(f"Heatmaps saved to '{output_folder}' folder.")
