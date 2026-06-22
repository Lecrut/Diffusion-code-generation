def print_filled_rectangle(width, height):
    row = '*' * width
    for _ in range(height):
        print(row)

if __name__ == '__main__':
    print_filled_rectangle(5, 3)