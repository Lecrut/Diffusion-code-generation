def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        line = ''
        for j in range(1, i + 1):
            line += str(j)
        print(line)

if __name__ == '__main__':
    print_number_pyramid(5)