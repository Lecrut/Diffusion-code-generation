import string

def generate_mirrored_triangle(rows: int) -> list:
    alphabet = string.ascii_uppercase
    result = []
    for i in range(1, rows + 1):
        segment = alphabet[:i]
        mirrored = segment + segment[::-1][1:]
        result.append(mirrored)
    return result

if __name__ == '__main__':
    sample_rows = 5
    output = generate_mirrored_triangle(sample_rows)
    for line in output:
        print(line)