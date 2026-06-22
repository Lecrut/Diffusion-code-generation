def check_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

if __name__ == '__main__':
    print(check_number(10))
    print(check_number(-5))
    print(check_number(0))