def print_square(number):
    return number ** 2

if __name__ == '__main__':
    for i in range(1, 21):
        square = print_square(i)
        print(square)