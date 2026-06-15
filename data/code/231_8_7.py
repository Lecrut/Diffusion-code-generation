import math
def generate_diamond(size):
    output = []
    center = size // 2
    for i in range(size * 2 - 1):
        row = ""
        if i < center:
            spaces = center - i
            stars = 2 * i + 1
            row = " " * spaces + "*" * stars
        else:
            spaces = i - center
            stars = 2 * (size - i) + 1
            row = " " * spaces + "*" * stars
        output.append(row)
    return "\n".join(output)
if __name__ == '__main__':
    sample_size = 7
    print(generate_diamond(sample_size))