import os

def concat_front():
    input_path = '/home/milos/Desktop/concatScript/front/input.txt'
    os.system("ffmpeg -f concat -safe 0 -i {} -c copy /home/milos/Desktop/concatScript/front/outputs/output_front.mp4".format(input_path))
    
concat_front()

def concat_left():
    input_path = '/home/milos/Desktop/concatScript/left/input.txt'
    os.system("ffmpeg -f concat -safe 0 -i {} -c copy /home/milos/Desktop/concatScript/left/outputs/output_left.mp4".format(input_path))
    
concat_left()

def concat_right():
    input_path = '/home/milos/Desktop/concatScript/right/input.txt'
    os.system("ffmpeg -f concat -safe 0 -i {} -c copy /home/milos/Desktop/concatScript/right/outputs/output_right.mp4".format(input_path))
    
concat_right()
