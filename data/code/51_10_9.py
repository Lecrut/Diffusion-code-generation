def print_number_pyramid():
    height = 5
    for row in range(1, height + 1):
        spaces = ' ' * (height - row)
        numbers = ''.join(str(num) for num in range(1, row + 1))
        print(f"{spaces}{numbers}")

if __name__ == '__main__':
    print_number_pyramid()