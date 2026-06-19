class VectorComparer:

    @staticmethod
    def is_elementwise_le(vector1, vector2):
        for i in range(min(len(vector1), len(vector2))):
            if vector1[i] > vector2[i]:
                return False
            elif vector1[i] < vector2[i]:
                return True
        return len(vector1) <= len(vector2)
if __name__ == '__main__':
    v1 = [1, 2, 3]
    v2 = [1, 2, 4]
    result = VectorComparer.is_elementwise_le(v1, v2)
    print(result)