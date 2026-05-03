class ValueComparator:
    def compare(self, val1, val2):
        if val1 > val2:
            return "val1 is greater"
        elif val1 < val2:
            return "val1 is less"
        else:
            return "val1 is equal"
if __name__ == '__main__':
    comparator = ValueComparator()
    result1 = comparator.compare(10, 5)
    print(f"Comparing 10 and 5: {result1}")
    result2 = comparator.compare(3, 3)
    print(f"Comparing 3 and 3: {result2}")
    result3 = comparator.compare(20, 15)
    print(f"Comparing 20 and 15: {result3}")
    result4 = comparator.compare(7, 12)
    print(f"Comparing 7 and 12: {result4}")