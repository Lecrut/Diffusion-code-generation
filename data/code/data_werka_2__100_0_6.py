SIGN_MAP = {
    1: "positive",
    -1: "negative",
    0: "zero"
}

def get_number_sign(value):
    if value > 0:
        sign = 1
    elif value < 0:
        sign = -1
    else:
        sign = 0
    return SIGN_MAP[sign]

if __name__ == '__main__':
    print(get_number_sign(15))
    print(get_number_sign(-10))
    print(get_number_sign(0))