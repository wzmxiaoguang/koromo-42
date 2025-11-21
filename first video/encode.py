from PIL import Image
import random


def shuffle(lst, restore=True):
    random.seed()
    random_number = []
    for i in range(len(lst) - 1, -1, -1):
        random_number.append(random.randint(0, i))
    for i in range(len(random_number)):
        if restore:
            lst[i], lst[random_number[i]] = lst[random_number[i]], lst[i]
        else:
            j = len(lst) - 1 - i
            lst[j], lst[random_number[j]] = lst[random_number[j]], lst[j]


def shuffle_pixels(image_path, output_path, restore=True):
    # 打开图片
    img = Image.open(image_path)
    # 获取图片的宽度和高度
    width, height = img.size
    # 将图片转换为像素访问模式
    pixels = img.load()
    # 创建一个与原图相同大小的列表来存储像素索引，以便于打乱顺序
    index = [(x, y) for y in range(height) for x in range(width)]
    pixel_indices = [(x, y) for y in range(height) for x in range(width)]

    shuffle(pixel_indices, restore)  # 打乱像素索引的顺序

    # 创建一个新的图像对象，用于存储最终的像素顺序
    new_img = Image.new('RGB', (width, height))
    new_pixels = new_img.load()


    # 根据打乱的索引重新排列像素
    for i in range(len(index)):
        new_pixels[index[i][0], index[i][1]] = pixels[pixel_indices[i][0], pixel_indices[i][1]]
    # 保存修改后的图片
    new_img.save(output_path)

if __name__ == '__main__':