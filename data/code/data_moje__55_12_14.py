def print_alphabet_triangle(n):
    result = []
    for i in range(1, n + 1):
        chars = [chr(ord('A') + j) for j in range(i)]
        result.append(" ".join(chars))
    return "\n".join(result)

if __name__ == '__main__':
    size = 5
    print(print_alphabet_triangle(size))