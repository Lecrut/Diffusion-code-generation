class QuantityComparer:
    def compare(self, q1, q2):
        diff = abs(q1 - q2)
        is_greater = q1 > q2
        return (diff, is_greater)
if __name__ == '__main__':
    comparer = QuantityComparer()
    qA = 10
    qB = 5
    result1 = comparer.compare(qA, qB)
    print(f"Comparing {qA} and {qB}: {result1}")
    qC = 3
    qD = 7
    result2 = comparer.compare(qC, qD)
    print(f"Comparing {qC} and {qD}: {result2}")
    qE = 4
    qF = 4
    result3 = comparer.compare(qE, qF)
    print(f"Comparing {qE} and {qF}: {result3}")