ZERO_VALUE = 0

def determine_sign(n):
    if n > ZERO_VALUE:
        return "positive"
    if n < ZERO_VALUE:
        return "negative"
    return "zero"

if __name__ == '__main__':
    print(determine_sign(15))
    print(determine_sign(-20))
    print(determine_sign(0))