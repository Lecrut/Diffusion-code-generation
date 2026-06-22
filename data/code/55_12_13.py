def generate_alphabet_triangle(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    triangle = []
    for i in range(1, size + 1):
        row = alphabet[0:i]
        triangle.append(row)
    return triangle

if __name__ == '__main__':
    result = generate_alphabet_triangle(5)
    for row in result:
        print(row)