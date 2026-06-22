class Vector:

    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def is_less_than_or_equal(cls, vec1, vec2):
        for e1, e2 in zip(vec1.elements, vec2.elements):
            if e1 > e2:
                return False
            elif e1 < e2:
                return True
        return True
if __name__ == '__main__':
    vector1 = Vector([1, 2, 3])
    vector2 = Vector([1, 3, 2])
    result = Vector.is_less_than_or_equal(vector1, vector2)
    print(result)