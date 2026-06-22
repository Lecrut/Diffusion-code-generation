import string

def generate_centered_alphabet_triangle(lines):
    alphabet = string.ascii_uppercase
    result = []
    for i in range(1, lines + 1):
        if i > len(alphabet):
            break
        current_row = alphabet[:i]
        padded_row = current_row.ljust(len(current_row) + (i - 1), " ")
        width = lines + (lines - 1)
        result.append(padded_row.center(width))
    return result

if __name__ == "__main__":
    sample_lines = 5
    print(generate_centered_alphabet_triangle(sample_lines))