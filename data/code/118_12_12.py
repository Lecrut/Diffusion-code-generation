class VectorCalculator:
    def __init__(self, vector):
        self.vector = vector
    
    def dot_product(self, other_vector):
        return sum(x * y for x, y in zip(self.vector, other_vector))

if __name__ == '__main__':
    vec1 = VectorCalculator([1, 3, -5])
    vec2 = VectorCalculator([4, -2, -1])
    result = vec1.dot_product(vec2)
    print(result)