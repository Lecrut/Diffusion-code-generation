import math
def generate_inverted_triangle(n):
    lines = []
    for i in range(n):
        line = ""
        leading_spaces = n - 1 - i
        stars = 2 * i + 1
        spaces = (n - stars) // 2
        line = " " * leading_spaces + "*" * stars + " " * spaces
        lines.append(line)
    return lines
if __name__ == '__main__':
    N = 5
    pattern = generate_inverted_triangle(N)
    for line in pattern:
        print(line)