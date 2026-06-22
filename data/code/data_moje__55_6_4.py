def print_hollow_alphabet_triangle(base_width):
    if base_width < 1:
        return
    for row in range(1, base_width + 1):
        line = []
        for col in range(1, base_width + 1):
            if row == 1:
                line.append(chr(ord('A') + col - 1))
            elif row == base_width:
                line.append(chr(ord('A') + col - 1))
            elif col == 1:
                line.append('A')
            elif col == row:
                line.append(chr(ord('A') + row - 1))
            else:
                line.append(' ')
        print("".join(line))

if __name__ == '__main__':
    print_hollow_alphabet_triangle(5)