from pathlib import Path
from rembg import remove, new_session

session = new_session()
input_dic = './input_img/'
output_dic = './output_img/'

for file in Path(input_dic).glob('*.jpg'):
    input_path = str(file)
    output_path = str(output_dic + (file.stem + ".out.png"))

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input, session=session)
            o.write(output)