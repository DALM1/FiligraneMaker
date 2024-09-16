from PIL import Image, ImageDraw, ImageFont

def ajouter_filigrane_multiple(image_path, texte_filigrane, output_path, interval=100):

    image = Image.open(image_path)

    image_filigrane = image.copy()

    largeur, hauteur = image.size

    draw = ImageDraw.Draw(image_filigrane)

    font = ImageFont.load_default()

    for y in range(0, hauteur, interval):
        for x in range(0, largeur, interval):

            position = (x, y)

            draw.text(position, texte_filigrane, font=font, fill=(255, 255, 255, 128))

    image_filigrane.save(output_path)

ajouter_filigrane_multiple('photo_identite.jpg', 'Confidentiel -- Confidentiel', 'photo_identite_filigranee_multiple.jpg', interval=100)
 
