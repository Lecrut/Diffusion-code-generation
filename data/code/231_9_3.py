import sys
def generate_square(size):
    pattern = []
    for y in range(size):
        row = []
        for x in range(size):
            if (x + y) % 2 == 0:
                row.append('#')
            else:
                row.append(' ')
        pattern.append("".join(row))
    return "\n".join(pattern)
if __name__ == '__main__':
    width = 10
    height = 10
    print(generate_square(width))