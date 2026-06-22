def print_alphabet_triangle(height):
    for row in range(1, height + 1):
        line = ""
        for col in range(row):
            line += chr(ord('A') + col)
        print(line)

if __name__ == '__main__':
    sample_height = 5
    print_alphabet_triangle(sample_height)