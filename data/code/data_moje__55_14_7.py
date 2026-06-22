def generate_centered_alphabet_triangle(rows: int=5) -> list:
    if rows <= 0:
        return []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_width = 2 * rows - 1
    result = []
    for i in range(rows):
        num_letters = 2 * i + 1
        letters = alphabet[:i + 1]
        pattern = letters + letters[-2::-1] if i > 0 else letters
        line = pattern.center(max_width)
        result.append(line)
    return result
if __name__ == '__main__':
    sample_rows = 5
    triangle = generate_centered_alphabet_triangle(sample_rows)
    for line in triangle:
        print(line)