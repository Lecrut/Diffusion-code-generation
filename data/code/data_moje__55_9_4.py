def generate_mirrored_alphabet_triangle(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in range(n):
        current_char = alphabet[i]
        left_part = ''.join([alphabet[j] for j in range(i + 1)])
        right_part = ''.join([alphabet[j] for j in range(i - 1, -1, -1)])
        row = left_part + right_part
        result.append(row)
    return result

if __name__ == '__main__':
    sample_n = 5
    result = generate_mirrored_alphabet_triangle(sample_n)
    for row in result:
        print(row)