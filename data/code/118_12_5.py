class Vector:
    def __init__(self, components):
        self.components = components

    def dot_product(self, other_vector):
        return sum(x * y for x, y in zip(self.components, other_vector.components))

if __name__ == '__main__':
    vec1 = Vector([1, 3, -5])
    vec2 = Vector([4, -2, -1])
    result = vec1.dot_product(vec2)
    print(result)