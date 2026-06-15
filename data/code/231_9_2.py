import sys
def generate_square(size):
    pattern = []
    for i in range(size):
        row = '*' * size
        pattern.append(row)
    return "\n".join(pattern)
if __name__ == '__main__':
    width = 10
    height = 10
    print(generate_square(width))
    print(generate_square(height))