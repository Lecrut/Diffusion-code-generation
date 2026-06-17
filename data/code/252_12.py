class QuantityComparator:
    def compare_and_display(self, q1, q2):
        if q1 > q2:
            print(f"{q1} is greater than {q2}")
        elif q2 > q1:
            print(f"{q2} is greater than {q1}")
        else:
            print(f"{q1} is equal to {q2}")
if __name__ == '__main__':
    comparator = QuantityComparator()
    comparator.compare_and_display(15, 10)
    comparator.compare_and_display(50, 75)
    comparator.compare_and_display(33, 33)