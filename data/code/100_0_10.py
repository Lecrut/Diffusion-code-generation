ZERO_VALUE = 0
SIGN_MAP = {1: "positive", -1: "negative", 0: "zero"}

def determine_sign(n):
    if n > ZERO_VALUE:
        return SIGN_MAP[1]
    if n < ZERO_VALUE:
        return SIGN_MAP[-1]
    return SIGN_MAP[0]

if __name__ == '__main__':
    print(determine_sign(15))
    print(determine_sign(-8))
    print(determine_sign(0))