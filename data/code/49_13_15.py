VALIDATION_CONSTANT = 6

class StarSquare:
    def __init__(self, dimension):
        self.dimension = dimension
        self._validate()
        self.line = '*' * self.dimension

    def _validate(self):
        if not isinstance(self.dimension, int) or self.dimension < 1:
            raise ValueError("Dimension must be a positive integer")

    def render(self):
        return '\n'.join([self.line] * self.dimension)

if __name__ == '__main__':
    square = StarSquare(VALIDATION_CONSTANT)
    print(square.render())