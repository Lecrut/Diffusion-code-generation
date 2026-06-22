import string

def generate_centered_alphabet_triangle(n):
    letters = string.ascii_lowercase
    triangle = []
    for i in range(n):
        part = letters[: i + 1]
        row = part + part[-2::-1]
        triangle.append(row.center(n * 2 - 1))
    return triangle

if __name__ == '__main__':
    result = generate_centered_alphabet_triangle(5)
    print(result)