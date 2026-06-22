import string

def generate_centered_alphabet_triangle(rows: int) -> list[str]:
    alphabet = string.ascii_uppercase
    result = []
    for i in range(rows):
        if i >= len(alphabet):
            break
        chars = list(alphabet[: i + 1])
        line = " ".join(chars)
        padding = " " * ((len(alphabet) + (rows - 1)) - len(line))
        result.append(padding[: len(line)] + line)
    return result

if __name__ == "__main__":
    sample_rows = 5
    pattern = generate_centered_alphabet_triangle(sample_rows)
    for line in pattern:
        print(line)