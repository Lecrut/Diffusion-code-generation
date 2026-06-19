class VectorComparator:

    @staticmethod
    def is_elementwise_le(vector1, vector2):
        for v1, v2 in zip(vector1, vector2):
            if v1 > v2:
                return False
        return True
if __name__ == '__main__':
    vec1 = [1, 2, 3]
    vec2 = [1, 3, 2]
    result = VectorComparator.is_elementwise_le(vec1, vec2)
    print(result)
    vec3 = [4, 5, 6]
    vec4 = [4, 5, 5]
    result = VectorComparator.is_elementwise_le(vec3, vec4)
    print(result)