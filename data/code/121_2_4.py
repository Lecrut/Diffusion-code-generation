class QuantityComparator:
    def compare_quantities(self, quantity1, quantity2):
        if len(quantity1) != len(quantity2):
            return "Quantities have different numbers of elements."
        if not quantity1:
            return "Both quantities are empty."
        sum1 = sum(quantity1)
        sum2 = sum(quantity2)
        if sum1 > sum2:
            return "Quantity 1 is larger."
        elif sum1 < sum2:
            return "Quantity 2 is larger."
        else:
            return "The quantities are equal in total size."
if __name__ == '__main__':
    comparator = QuantityComparator()
    q1 = [10, 20, 30]
    q2 = [5, 15, 25]
    q3 = [1, 2, 3]
    q4 = [10, 10, 10]
    q5 = [5, 5, 5]
    q6 = [10, 20]
    print(f"Comparing {q1} and {q2}: {comparator.compare_quantities(q1, q2)}")
    print(f"Comparing {q3} and {q4}: {comparator.compare_quantities(q3, q4)}")
    print(f"Comparing {q5} and {q1}: {comparator.compare_quantities(q5, q1)}")
    print(f"Comparing {q6} and {q1}: {comparator.compare_quantities(q6, q1)}")
    print(f"Comparing {q1} and [1, 2, 3, 4]: {comparator.compare_quantities(q1, [1, 2, 3, 4])}")
    print(f"Comparing [] and []: {comparator.compare_quantities([], [])}")