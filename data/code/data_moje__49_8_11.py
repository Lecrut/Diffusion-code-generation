def print_square():
    size = 9
    row = 0
    while row < size:
        print("*" * size)
        row += 1

if __name__ == '__main__':
    result = print_square()
    print(result)