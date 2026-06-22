class Vector:

    def __init__(self, data):
        self.data = data

    @classmethod
    def is_less_or_equal(cls, vector1, vector2):
        for v1, v2 in zip(vector1.data, vector2.data):
            if v1 > v2:
                return False
            elif v1 < v2:
                return True
        return True
if __name__ == '__main__':
    vec1 = Vector([1, 2, 3])
    vec2 = Vector([1, 3, 2])
    result = Vector.is_less_or_equal(vec1, vec2)
    print(result)