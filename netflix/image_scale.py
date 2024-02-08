from PIL import Image

# 1번 이미지의 크기를 얻습니다.
with Image.open("./main-img/TVshow-1.jpg") as img:
    width, height = img.size

# 2부터 8번 이미지까지 크기를 조정합니다.
for i in range(2, 7):
    filename = f"./main-img/TVshow-{i}.jpg"
    with Image.open(filename) as img:
        # 크기를 1번 이미지와 동일하게 조정합니다.
        resized_img = img.resize((width, height))
        # 크기를 조정한 이미지를 덮어쓰기합니다.
        resized_img.save(filename)

print("이미지 크기를 조정하였습니다.")
