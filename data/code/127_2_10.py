def is_odd(number: int) -> bool:
    return number & 1
if __name__ == '__main__':
    print(is_odd(3))
    print(is_odd(4))