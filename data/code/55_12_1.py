def generate_alphabet_triangle(rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in range(rows):
        current_row = "".join(alphabet[j % len(alphabet)] for j in range(i + 1))
        result.append(current_row)
    return "\n".join(result)

if __name__ == "__main__":
    sample_rows = 5
    print(generate_alphabet_triangle(sample_rows))