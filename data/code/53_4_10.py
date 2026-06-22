from itertools import chain

def reverse_number_triangle(height=3):
    for i in range(height, 0, -1):
        digits = list(range(1, i + 1))
        reversed_digits = digits[::-1]
        row_digits = list(chain(digits, reversed_digits[1:]))
        yield ''.join(map(str, row_digits))

if __name__ == '__main__':
    result = list(reverse_number_triangle(3))
    for row in result:
        print(row)