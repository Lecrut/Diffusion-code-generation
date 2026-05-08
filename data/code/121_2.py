class QuantityComparator:
    def compare_quantities(self, quantity1, quantity2):
        if len(quantity1) != len(quantity2):
            return "Quantities have different numbers of elements."
        if not quantity1:
            return "Both quantities are empty."
        sum1 = sum(quantity1)
        sum2 = sum(quantity2)
        if sum1 > sum2:
            return f"Quantity 1 (sum: {sum1}) is larger than Quantity 2 (sum: {sum2})."
        elif sum1 < sum2:
            return f"Quantity 1 (sum: {sum1}) is smaller than Quantity 2 (sum: {sum2})."
        else:
            return f"Quantity 1 (sum: {sum1}) is equal to Quantity 2 (sum: {sum2})."
if __name__ == '__main__':
    comparator = QuantityComparator()
    q1 = [10, 20, 30]
    q2 = [5, 15, 25]
    q3 = [1, 2, 3]
    q4 = [10, 10, 10]
    q5 = [5, 5]
    print(comparator.compare_quantities(q1, q2))
    print(comparator.compare_quantities(q3, q4))
    print(comparator.compare_quantities(q1, q5))
    print(comparator.compare_quantities(q2, q1))
    print(comparator.compare_quantities(q5, q5))
    print(comparator.compare_quantities([1, 2], [1, 2, 3]))
    print(comparator.compare_quantities([], []))