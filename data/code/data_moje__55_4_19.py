def generate_alphabet_pyramid(rows):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lines = [
        ' ' * (rows - i) + ' '.join(alphabet[j] for j in range(2 * i - 1))
        for i in range(1, rows + 1)
    ]
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_alphabet_pyramid(5))