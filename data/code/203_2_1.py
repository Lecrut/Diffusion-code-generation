class QuantityComparator:
    def compare(self, quantity1, quantity2):
        name1, value1 = quantity1
        name2, value2 = quantity2
        if value1 > value2:
            return quantity1
        elif value2 > value1:
            return quantity2
        else:
            return quantity1
if __name__ == '__main__':
    comparator = QuantityComparator()
    q1 = ("Apples", 10)
    q2 = ("Bananas", 15)
    q3 = ("Oranges", 10)
    q4 = ("Grapes", 20)
    result1 = comparator.compare(q1, q2)
    print(f"Comparing {q1} and {q2}: {result1}")
    result2 = comparator.compare(q3, q4)
    print(f"Comparing {q3} and {q4}: {result2}")
    result3 = comparator.compare(q1, q3)
    print(f"Comparing {q1} and {q3}: {result3}")