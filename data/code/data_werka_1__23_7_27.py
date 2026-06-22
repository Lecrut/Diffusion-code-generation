class Vector:
    def __init__(self, data):
        self.data = data

    @classmethod
    def is_less_than_or_equal(cls, vec1, vec2):
        for i in range(min(len(vec1.data), len(vec2.data))):
            if vec1.data[i] > vec2.data[i]:
                return False
            elif vec1.data[i] < vec2.data[i]:
                return True
        return len(vec1.data) <= len(vec2.data)

if __name__ == '__main__':
    vector1 = Vector([1, 2, 3])
    vector2 = Vector([1, 2, 4])
    result = Vector.is_less_than_or_equal(vector1, vector2)
    print(result)