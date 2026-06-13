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
    quantity_a = ("Apple", 50)
    quantity_b = ("Banana", 120)
    quantity_c = ("Carrot", 30)
    result1 = comparator.compare(quantity_a, quantity_b)
    print(f"Comparing {quantity_a} and {quantity_b}: {result1}")
    result2 = comparator.compare(quantity_c, quantity_a)
    print(f"Comparing {quantity_c} and {quantity_a}: {result2}")
    result3 = comparator.compare(quantity_b, quantity_c)
    print(f"Comparing {quantity_b} and {quantity_c}: {result3}")
    result4 = comparator.compare(quantity_a, quantity_a)
    print(f"Comparing {quantity_a} and {quantity_a}: {result4}")