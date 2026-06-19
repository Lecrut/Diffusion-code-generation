class VectorComparison:

    @staticmethod
    def is_less_than_or_equal(vector1, vector2):
        for v1, v2 in zip(vector1, vector2):
            if v1 > v2:
                return False
            elif v1 < v2:
                return True
        return True
if __name__ == '__main__':
    vector_a = [1, 2, 3]
    vector_b = [1, 3, 2]
    result = VectorComparison.is_less_than_or_equal(vector_a, vector_b)
    print(result)