from ultralytics import YOLO
model=YOLO("yolov8x")
result = model.predict("input_videos/input_video.mp4", save=True)
