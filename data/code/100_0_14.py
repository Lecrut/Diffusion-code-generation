ZERO_THRESHOLD = 0

def determine_sign(n):
    if n > ZERO_THRESHOLD:
        return "positive"
    if n < ZERO_THRESHOLD:
        return "negative"
    return "zero"

if __name__ == '__main__':
    print(determine_sign(15))
    print(determine_sign(-8))
    print(determine_sign(0))