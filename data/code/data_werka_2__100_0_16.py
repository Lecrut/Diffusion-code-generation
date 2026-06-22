def determine_sign(number):
    if number > 0:
        return "positive"
    if number < 0:
        return "negative"
    return "zero"

if __name__ == '__main__':
    print(determine_sign(0))
    print(determine_sign(15))
    print(determine_sign(-20))