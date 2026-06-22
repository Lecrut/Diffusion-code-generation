def generate_centered_alphabet_triangle(size=4):
    letters = [chr(ord('A') + i) for i in range(size)]
    result = []
    max_width = 2 * size - 1
    for i in range(size):
        current_line = ' '.join(letters[j] for j in range(2 * i + 1))
        result.append(current_line.center(max_width * 2 - 1))
    return result

if __name__ == '__main__':
    print(generate_centered_alphabet_triangle())