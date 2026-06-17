class QuantityComparator:
    def compare(self, quantity1, quantity2):
        if quantity1 > quantity2:
            return f"{quantity1} is greater than {quantity2}"
        elif quantity2 > quantity1:
            return f"{quantity2} is greater than {quantity1}"
        else:
            return f"{quantity1} is equal to {quantity2}"
if __name__ == '__main__':
    comparator = QuantityComparator()
    q1 = 10
    q2 = 5
    print(comparator.compare(q1, q2))
    q3 = 20
    q4 = 20
    print(comparator.compare(q3, q4))
    q5 = 3.14
    q6 = 3.14159
    print(comparator.compare(q5, q6))