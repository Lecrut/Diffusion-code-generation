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
    qA = ("Apple", 10)
    qB = ("Banana", 5)
    qC = ("Cherry", 15)
    qD = ("Date", 10)
    result1 = comparator.compare(qA, qB)
    print(f"Comparing {qA} and {qB}: {result1}")
    result2 = comparator.compare(qC, qD)
    print(f"Comparing {qC} and {qD}: {result2}")
    result3 = comparator.compare(qA, qC)
    print(f"Comparing {qA} and {qC}: {result3}")