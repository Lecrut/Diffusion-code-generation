class Vector:
    def __init__(self, data):
        self.data = data

    def dot_product(self, other):
        return sum(x * y for x, y in zip(self.data, other.data))

if __name__ == '__main__':
    v1 = Vector([1, 3, -5])
    v2 = Vector([4, -2, -1])
    result = v1.dot_product(v2)
    print(result)