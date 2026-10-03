import qrcode

url = "https://petrickbrayan.github.io/presente-amorzinho/"

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=14,
    border=5,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image()
path = "/mnt/data/qr_code_presente_amorzinho.png"
img.save(path)

print(path)
