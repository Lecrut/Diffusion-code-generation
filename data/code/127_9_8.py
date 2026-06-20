ODD_CHECK = 1

def is_odd(num):
    return num & ODD_CHECK == ODD_CHECK

if __name__ == '__main__':
    print(is_odd(3))
    print(is_odd(4))