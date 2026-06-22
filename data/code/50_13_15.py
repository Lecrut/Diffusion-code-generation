def validate_size(n):
    if not isinstance(n, int):
        raise TypeError("Size must be an integer")
    if n < 1:
        raise ValueError("Size must be a positive integer")
    return n

def format_row(count):
    return '*' * count

def construct_inverted_triangle(n):
    validate_size(n)
    return '\n'.join(format_row(i) for i in range(n, 0, -1))

class TriangleBuilder:
    def __init__(self, size):
        self.size = size

    def build(self):
        return construct_inverted_triangle(self.size)

if __name__ == '__main__':
    builder = TriangleBuilder(5)
    print(builder.build())