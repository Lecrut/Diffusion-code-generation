def generate_zigzag_triangle(rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in range(rows):
        line = []
        for j in range(i + 1):
            index = j if j % 2 == 0 else i - j
            if index < len(alphabet):
                line.append(alphabet[index])
            else:
                line.append(alphabet[index % len(alphabet)])
        result.append(" ".join(line))
    return result

if __name__ == "__main__":
    sample_rows = 6
    lines = generate_zigzag_triangle(sample_rows)
    for line in lines:
        print(line)