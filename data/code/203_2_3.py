class QuantityComparator:
    def compare(self, q1, q2):
        name1, value1 = q1
        name2, value2 = q2
        if value1 > value2:
            return q1
        elif value2 > value1:
            return q2
        else:
            return q1
if __name__ == '__main__':
    comparator = QuantityComparator()
    q_a = ("Apple", 10)
    q_b = ("Banana", 5)
    q_c = ("Orange", 10)
    q_d = ("Grape", 20)
    result1 = comparator.compare(q_a, q_b)
    print(f"Comparing {q_a} and {q_b}: {result1}")
    result2 = comparator.compare(q_c, q_d)
    print(f"Comparing {q_c} and {q_d}: {result2}")
    result3 = comparator.compare(q_a, q_c)
    print(f"Comparing {q_a} and {q_c}: {result3}")