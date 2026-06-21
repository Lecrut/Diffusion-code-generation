def hex_to_decimal(hex_code):
    return int(hex_code, 16)

def map_hex_to_decimal():
    hex_colors = {
        "red": "#FF0000",
        "green": "#00FF00",
        "blue": "#0000FF",
        "white": "#FFFFFF",
        "black": "#000000"
    }
    return {name: hex_to_decimal(code.lstrip('#')) for name, code in hex_colors.items()}

if __name__ == '__main__':
    result = map_hex_to_decimal()
    print(result)