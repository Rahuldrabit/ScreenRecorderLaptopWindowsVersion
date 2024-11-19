import cv2
import numpy as np
import pyautogui

# Get screen resolution
SCREEN_SIZE = tuple(pyautogui.size())

# Define video codec (XVID) and frames per second (FPS)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 26.0

# Create a VideoWriter object
out = cv2.VideoWriter("Recording.avi", fourcc, fps, SCREEN_SIZE)

# Record for 10 seconds (adjust as needed)
record_seconds = 300

for i in range(int(record_seconds * fps)):
    # Capture screenshot
    img = pyautogui.screenshot()

    # Convert pixels to a numpy array
    frame = np.array(img)

    # Convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video file
    out.write(frame)

    # Show the frame (optional)
    cv2.imshow("screenshot", frame)

    # Exit if the user presses 'q'
    if cv2.waitKey(1) == ord("q"):
        break

# Release the writer and close all windows
out.release()
cv2.destroyAllWindows()
