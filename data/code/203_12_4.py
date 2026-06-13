class QuantityComparer:
    def compare(self, q1, q2):
        absolute_difference = abs(q1 - q2)
        is_q1_greater = q1 > q2
        return (absolute_difference, is_q1_greater)
if __name__ == '__main__':
    comparer = QuantityComparer()
    q_a = 10
    q_b = 5
    result1 = comparer.compare(q_a, q_b)
    print(f"Comparing {q_a} and {q_b}: Difference={result1[0]}, Is {q_a} > {q_b} = {result1[1]}")
    q_c = 3
    q_d = 8
    result2 = comparer.compare(q_c, q_d)
    print(f"Comparing {q_c} and {q_d}: Difference={result2[0]}, Is {q_c} > {q_d} = {result2[1]}")
    q_e = 7
    q_f = 7
    result3 = comparer.compare(q_e, q_f)
    print(f"Comparing {q_e} and {q_f}: Difference={result3[0]}, Is {q_e} > {q_f} = {result3[1]}")