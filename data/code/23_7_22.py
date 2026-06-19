class Vector:
    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def is_less_or_equal(cls, vector1, vector2):
        for e1, e2 in zip(vector1.elements, vector2.elements):
            if e1 > e2:
                return False
            elif e1 < e2:
                return True
        return True

if __name__ == '__main__':
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 3, 2])
    result = Vector.is_less_or_equal(v1, v2)
    print(result)