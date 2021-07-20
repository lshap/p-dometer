import os
import subprocess


def main():
    os.chdir("p")
    _convert_videos_to_images()
    os.chdir("../no_p")
    _convert_videos_to_images()


def _convert_videos_to_images():
    for (i, p_video_file) in enumerate(os.listdir(".")):
        if ".mov" in p_video_file or ".MOV" in p_video_file:
            print(f"video file {p_video_file}")
            subprocess.run(
                ["ffmpeg", "-i", p_video_file, "-vf", "scale=96:170", "out.mp4"]
            )
            subprocess.run(
                ["ffmpeg", "-i", "out.mp4", "-filter:v", "crop=96:96:0:37", "out2.mp4"]
            )
            subprocess.run(["ffmpeg", "-i", "out2.mp4", "-vf", "hue=s=0", "out3.mp4"])
            subprocess.run(f'ffmpeg -i out3.mp4 "images/out-{i}-%03d.jpg"', shell=True)
            subprocess.run(["rm", "out.mp4"])
            subprocess.run(["rm", "out2.mp4"])
            subprocess.run(["rm", "out3.mp4"])


if __name__ == "__main__":
    main()
