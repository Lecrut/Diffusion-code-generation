def generate_centered_alphabet_triangle():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    triangle = []
    for i in range(len(alphabet)):
        segment = alphabet[:i + 1]
        line = " " * (len(alphabet) - i - 1) + segment
        triangle.append(line)
    return triangle

if __name__ == '__main__':
    result = generate_centered_alphabet_triangle()
    for line in result:
        print(line)