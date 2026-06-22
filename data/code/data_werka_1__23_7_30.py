class Vector:

    def __init__(self, data):
        self.data = data

    @classmethod
    def is_elementwise_le(cls, vec1, vec2):
        for a, b in zip(vec1.data, vec2.data):
            if a > b:
                return False
            elif a < b:
                return True
        return True
if __name__ == '__main__':
    vector1 = Vector([1, 2, 3])
    vector2 = Vector([1, 3, 2])
    result = Vector.is_elementwise_le(vector1, vector2)
    print(result)