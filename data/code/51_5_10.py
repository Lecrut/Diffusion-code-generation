def print_hollow_pyramid(rows):
    for i in range(1, rows + 1):
        leading_spaces = ' ' * (rows - i)
        if i == 1:
            print(leading_spaces + '*')
        elif i == rows:
            print(leading_spaces + '*' + ' *' * (i - 1))
        else:
            middle_spaces = ' ' * (2 * i - 3)
            print(leading_spaces + '*' + middle_spaces + '*')

if __name__ == '__main__':
    print_hollow_pyramid(5)