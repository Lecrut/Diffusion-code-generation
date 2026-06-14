import sys
def generate_square_pattern(size, repetitions):
    pattern = []
    for _ in range(repetitions):
        row = ""
        for i in range(size):
            row += "*" * size
        pattern.append(row)
    return "\n".join(pattern)
if __name__ == '__main__':
    square_size = 5
    repetitions = 3
    result = generate_square_pattern(square_size, repetitions)
    print(result)