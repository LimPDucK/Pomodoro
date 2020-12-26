from PIL import Image

image = Image.open('mylocker.png')
print(image.size)

image.save('mylocker.ico', sizes=[(200, 200)])
change_image = Image.open('mylocker.png')
print(change_image)
