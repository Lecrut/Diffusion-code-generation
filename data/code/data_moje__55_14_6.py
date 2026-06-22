def generate_centered_alphabet_triangle(rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in range(rows):
        if i >= len(alphabet):
            break
        char = alphabet[i]
        padding = rows - 1 - i
        line = " " * padding + char + " " * padding
        result.append(line)
    return result

if __name__ == "__main__":
    sample_rows = 5
    output = generate_centered_alphabet_triangle(sample_rows)
    for line in output:
        print(line)