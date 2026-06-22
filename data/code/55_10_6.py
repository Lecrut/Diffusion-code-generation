def print_alphabet_triangle(height):
    result = []
    for i in range(height):
        row_chars = [chr(ord('A') + (i + j) % 26) for j in range(i + 1)]
        row_str = ' '.join(row_chars)
        result.append(row_str)
    return result

if __name__ == '__main__':
    height = 5
    lines = print_alphabet_triangle(height)
    for line in lines:
        print(line)