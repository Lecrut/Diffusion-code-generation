def print_alphabet_triangle(n):
    for i in range(1, n + 1):
        line = ""
        for j in range(i):
            line += chr(65 + j)
        print(line)

if __name__ == '__main__':
    print_alphabet_triangle(5)