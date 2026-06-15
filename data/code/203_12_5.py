class QuantityComparer:
    def compare(self, q1, q2):
        absolute_difference = abs(q1 - q2)
        is_greater = q1 > q2
        return (absolute_difference, is_greater)
if __name__ == '__main__':
    comparer = QuantityComparer()
    q_a = 10
    q_b = 5
    result1 = comparer.compare(q_a, q_b)
    print(f"Comparing {q_a} and {q_b}: {result1}")
    q_c = 3.5
    q_d = 3.5
    result2 = comparer.compare(q_c, q_d)
    print(f"Comparing {q_c} and {q_d}: {result2}")
    q_e = -2
    q_f = 4
    result3 = comparer.compare(q_e, q_f)
    print(f"Comparing {q_e} and {q_f}: {result3}")