def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        print(str(i) * i)

if __name__ == '__main__':
    rows = 5
    result = print_number_pyramid(rows)