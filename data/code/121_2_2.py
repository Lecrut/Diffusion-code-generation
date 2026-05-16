class QuantityComparator:
    def compare_quantities(self, quantity1, quantity2):
        size1 = len(quantity1)
        size2 = len(quantity2)
        if size1 > size2:
            return f"Quantity 1 (size {size1}) is larger than Quantity 2 (size {size2})"
        elif size2 > size1:
            return f"Quantity 2 (size {size2}) is larger than Quantity 1 (size {size1})"
        else:
            return f"Quantity 1 (size {size1}) is equal to Quantity 2 (size {size2})"
if __name__ == '__main__':
    comparator = QuantityComparator()
    q1 = [1, 2, 3, 4]
    q2 = [5, 6]
    q3 = [10, 20, 30]
    q4 = [1, 2, 3, 4]
    print(comparator.compare_quantities(q1, q2))
    print(comparator.compare_quantities(q2, q1))
    print(comparator.compare_quantities(q3, q1))
    print(comparator.compare_quantities(q4, q4))
    print(comparator.compare_quantities(q2, q3))