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
    qA = ("Apple", 5)
    qB = ("Banana", 10)
    qC = ("Cherry", 7)
    result1 = comparator.compare(qA, qB)
    print(f"Comparing {qA} and {qB}: {result1}")
    result2 = comparator.compare(qC, qA)
    print(f"Comparing {qC} and {qA}: {result2}")
    result3 = comparator.compare(qB, qC)
    print(f"Comparing {qB} and {qC}: {result3}")
    result4 = comparator.compare(qA, qA)
    print(f"Comparing {qA} and {qA}: {result4}")