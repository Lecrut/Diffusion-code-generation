SIDE_LENGTH = 6
UNIT_MAP = {
    "meters": "m",
    "centimeters": "cm",
    "feet": "ft"
}

def get_area(side):
    return side ** 2

if __name__ == '__main__':
    side_val = SIDE_LENGTH
    result = get_area(side_val)
    unit_symbol = UNIT_MAP["meters"]
    print(f"{result} {unit_symbol}^2")