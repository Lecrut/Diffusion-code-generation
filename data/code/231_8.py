import math
def generate_diamond(size):
    output = []
    for i in range(size * 2 - 1):
        line = ""
        if i < size:
            spaces = " " * (size - i)
            stars = "*" * (2 * i + 1)
            line = spaces + stars
        else:
            spaces = " " * (2 * (size - i) - 1)
            stars = "*" * (2 * (size - i) - 1)
            line = spaces + stars
        output.append(line)
    return output
if __name__ == '__main__':
    diamond_size = 5
    pattern = generate_diamond(diamond_size)
    for line in pattern:
        print(line)