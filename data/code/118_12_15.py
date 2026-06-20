class VectorMultiplier:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def calculate_dot_product(self):
        return sum(x * y for x, y in zip(self.v1, self.v2))

if __name__ == '__main__':
    vector_multiplier = VectorMultiplier([1, 3, -5], [4, -2, -1])
    result = vector_multiplier.calculate_dot_product()
    print(result)