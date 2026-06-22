def print_pyramid():
    for i in range(1, 6):
        print("  " * (5 - i) + (str(i) + " ") * (2 * i - 1))

if __name__ == '__main__':
    print_pyramid()