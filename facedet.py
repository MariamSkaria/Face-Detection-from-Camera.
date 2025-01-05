import cv2
def detfacecamera():
    cap = cv2.VideoCapture(0) 
    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return
   
