class VectorComparator:
    @staticmethod
    def compare_elementwise_le(vec1, vec2):
        n = len(vec1)
        if len(vec2) != n:
            return False
        for i in range(n):
            if vec1[i] > vec2[i]:
                return False
            if vec1[i] < vec2[i]:
                return True
        return True
if __name__ == '__main__':
    vec_a = [1, 5, 3]
    vec_b = [1, 4, 3]
    vec_c = [2, 5, 3]
    vec_d = [1, 5, 4]
    vec_e = [1, 5, 3]
    vec_f = [1, 5, 3]
    vec_g = [1, 5, 5]
    print(f"Compare {vec_a} and {vec_b}: {VectorComparator.compare_elementwise_le(vec_a, vec_b)}")
    print(f"Compare {vec_a} and {vec_c}: {VectorComparator.compare_elementwise_le(vec_a, vec_c)}")
    print(f"Compare {vec_a} and {vec_d}: {VectorComparator.compare_elementwise_le(vec_a, vec_d)}")
    print(f"Compare {vec_a} and {vec_e}: {VectorComparator.compare_elementwise_le(vec_a, vec_e)}")
    print(f"Compare {vec_a} and {vec_f}: {VectorComparator.compare_elementwise_le(vec_a, vec_f)}")
    print(f"Compare {vec_a} and {vec_g}: {VectorComparator.compare_elementwise_le(vec_a, vec_g)}")