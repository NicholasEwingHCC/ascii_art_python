from PIL import Image

img = Image.open("images/download.jpeg").convert('L')

size = tuple(int(ti / 2) for ti in img.size)
img = img.resize(size, Image.ANTIALIAS)

characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" # 64

pixels = list(img.getdata(0))

counter = 0
for line in range(img.height):
    answer = []
    for i in range(img.width):
        char_index = int(pixels[counter] / 4)
        if char_index > 64:
            char_index = 64
        answer.append(characters[char_index] * 2)
        counter += 1
    print("".join(answer))

