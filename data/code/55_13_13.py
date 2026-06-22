def print_triangle(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(n):
        row = []
        for j in range(i + 1):
            char_index = (i * (i + 1) // 2 + j) % 26
            row.append(alphabet[char_index])
        print(" ".join(row))

if __name__ == '__main__':
    print_triangle(5)