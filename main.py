import qrcode

img = qrcode.make(
    input("What would you like to convert into a QR Code ?\n > "))
name = input("What would you like to name the file ? \n > ")

type(img)
img.save(f"./GeneratedQrCodes/{name}.png")
