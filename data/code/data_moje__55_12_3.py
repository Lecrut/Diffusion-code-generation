import string

def generate_alphabet_triangle(rows):
    alphabet = string.ascii_uppercase
    triangle = []
    for i in range(1, rows + 1):
        chars = alphabet[:i]
        line = ' '.join(chars)
        triangle.append(line)
    return '\n'.join(triangle)

if __name__ == '__main__':
    result = generate_alphabet_triangle(5)
    print(result)