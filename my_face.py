import face_recognition
from shutil import copyfile
import multiprocessing as mp

def solution():
    # Create an encoding of my facial features that can be compared to other faces

    picture_of_me = face_recognition.load_image_file('/path to target_photo.jpg')
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    # Iterate through all the  pictures

    for i in range(1,4607):
        # Construct the picture name and print it
        file_name = str(i).zfill(5) + ".jpg"
        print(file_name)

        #load this picture
        new_picture = face_recognition.load_image_file('/path to photo files' + file_name)

        #iterate through every fave detected in the new picture
        for face_encoding in face_recognition.face_encodings(new_picture):
            # Run the algorithm of face comparison for the detected face, with 0.5 tolerance
            results = face_recognition.compare_faces([my_face_encoding], face_encoding, 0.5)

            #save the image to a separate folder if there is a match
            if results[0] == True:
                copyfile('/path to photo files' + file_name, "/path where you want the result pasted" + file_name)


if __name__ == "__main__":
    solution()
