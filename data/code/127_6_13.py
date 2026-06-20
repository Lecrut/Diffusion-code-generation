def verify_oddity(number):
    return number & 1 == 1
if __name__ == '__main__':
    print(verify_oddity(3))
    print(verify_oddity(4))