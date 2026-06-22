def get_hollow_alphabet_triangle(n):
    if n <= 0:
        return ""
    result = []
    for i in range(1, n + 1):
        if i == 1:
            row = "A"
        elif i == n:
            row = ""
            for j in range(i):
                row += chr(ord('A') + (j % 26))
        elif i == 2:
            row = "A"
            for j in range(1, i - 1):
                row += " "
            row += "B"
        else:
            left_char = chr(ord('A') + (i - 2) % 26)
            right_char = chr(ord('A') + (i - 1) % 26)
            row = left_char
            for j in range(1, i - 1):
                row += " "
            row += right_char
        result.append(row)
    return "\n".join(result)

if __name__ == '__main__':
    n = 5
    print(get_hollow_alphabet_triangle(n))