class VectorComparer:
    @staticmethod
    def is_less_or_equal(vector1, vector2):
        for i in range(min(len(vector1), len(vector2))):
            if vector1[i] > vector2[i]:
                return False
            elif vector1[i] < vector2[i]:
                return True
        return len(vector1) <= len(vector2)

if __name__ == '__main__':
    vector_a = [1, 2, 3]
    vector_b = [1, 2, 4]
    result = VectorComparer.is_less_or_equal(vector_a, vector_b)
    print(result)