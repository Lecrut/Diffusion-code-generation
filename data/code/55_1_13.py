import string

def print_centered_alphabet_triangle(height):
    if height <= 0:
        return ""
    alphabet = string.ascii_uppercase
    if height > len(alphabet):
        height = len(alphabet)
    lines = []
    for i in range(height):
        letters = "".join(alphabet[j] for j in range(i + 1))
        line = letters.center(height * 2 - 1)
        lines.append(line)
    result = "\n".join(lines)
    print(result)
    return result

if __name__ == "__main__":
    print_centered_alphabet_triangle(5)