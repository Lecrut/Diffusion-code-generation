def print_alphabet_triangle(n):
    for i in range(1, n + 1):
        chars = [chr(65 + j) for j in range(i)]
        print(" ".join(chars))

if __name__ == '__main__':
    print_alphabet_triangle(5)