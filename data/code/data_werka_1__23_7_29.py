class VectorComparator:

    @staticmethod
    def is_less_or_equal(vector1, vector2):
        for v1, v2 in zip(vector1, vector2):
            if v1 > v2:
                return False
            elif v1 < v2:
                return True
        return True
if __name__ == '__main__':
    vec1 = [1, 2, 3]
    vec2 = [1, 3, 2]
    result = VectorComparator.is_less_or_equal(vec1, vec2)
    print(result)