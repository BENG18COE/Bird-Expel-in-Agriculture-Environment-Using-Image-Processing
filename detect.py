from device.FaceRecognition import FaceRecognition

if __name__ == "__main__":
    # FaceRecognition().faces_encoding()

    face_recognizer = FaceRecognition(
        encodings="encodings/encodings.pickle",
    )
    face_recognizer.faces_detection()