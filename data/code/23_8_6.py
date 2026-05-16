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
    print(f"Comparing {vec_a} and {vec_b}: {VectorComparator.compare_elementwise_le(vec_a, vec_b)}")
    vec_c = [1, 5, 3]
    vec_d = [1, 5, 4]
    print(f"Comparing {vec_c} and {vec_d}: {VectorComparator.compare_elementwise_le(vec_c, vec_d)}")
    vec_e = [2, 5, 3]
    vec_f = [1, 5, 3]
    print(f"Comparing {vec_e} and {vec_f}: {VectorComparator.compare_elementwise_le(vec_e, vec_f)}")
    vec_g = [1, 5, 3]
    vec_h = [1, 5, 3]
    print(f"Comparing {vec_g} and {vec_h}: {VectorComparator.compare_elementwise_le(vec_g, vec_h)}")
    vec_i = [1, 5, 3]
    vec_j = [1, 6, 3]
    print(f"Comparing {vec_i} and {vec_j}: {VectorComparator.compare_elementwise_le(vec_i, vec_j)}")
    vec_k = [1, 5, 3]
    vec_l = [1, 5, 2]
    print(f"Comparing {vec_k} and {vec_l}: {VectorComparator.compare_elementwise_le(vec_k, vec_l)}")
    vec_m = [1, 5, 3]
    vec_n = [2, 5, 3]
    print(f"Comparing {vec_m} and {vec_n}: {VectorComparator.compare_elementwise_le(vec_m, vec_n)}")
    vec_o = [1, 5, 3]
    vec_p = [1, 5, 5]
    print(f"Comparing {vec_o} and {vec_p}: {VectorComparator.compare_elementwise_le(vec_o, vec_p)}")