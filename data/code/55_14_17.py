def generate_alphabet_triangle():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    max_width = 2 * len(alphabet) - 1
    for i in range(len(alphabet)):
        chars = []
        for j in range(len(alphabet)):
            if j <= i:
                chars.append(alphabet[j])
            else:
                chars.append(alphabet[i])
        row_str = ''.join(chars)
        spaces = (max_width - len(row_str)) // 2
        line = ' ' * spaces + row_str + ' ' * spaces
        result.append(line.strip())
    return result

if __name__ == '__main__':
    output = generate_alphabet_triangle()
    print('\n'.join(output))