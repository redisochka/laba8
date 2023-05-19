from PIL import Image, ImageDraw, ImageFont

def xd1():

    photo = Image.open('photo.jpg')
    cropped_photo = photo.crop((100,10, 1190, 600))
    cropped_photo.save('cropped_photo.png')

def xd2():

    cards = {"23 февраля": "23f.jpg", "8 Марта": "8m.jpg"}
    holiday = input("Введите название праздника: ")
    card_file = cards.get(holiday)
    if not card_file:
        print("Открытка не найдена")
    else:
        card = Image.open(card_file)
        card.show()

def xd3():

    photo = Image.open('photo.jpg')
    cropped_photo = photo.crop((100, 10, 1190, 600))

    name = input("Введите имя: ")
    draw = ImageDraw.Draw(cropped_photo)
    text = f"{name}, поздравляю!"

    font = ImageFont.truetype("arial.ttf", 40)
    color = (255, 255, 255)
    textwidth, textheight = draw.textsize(text, font)
    x = (cropped_photo.width - textwidth) - 20
    y = textheight
    draw.text((x, y), text, font=font, fill=color)

    cropped_photo.save("cropped_img_with_text.png")


xd1()
xd2()
xd3()