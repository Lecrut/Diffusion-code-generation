class ValueComparator:
    def compare(self, val1, val2):
        if val1 > val2:
            return f"{val1} is greater than {val2}"
        elif val1 < val2:
            return f"{val1} is less than {val2}"
        else:
            return f"{val1} is equal to {val2}"

if __name__ == '__main__':
    comparator = ValueComparator()
    result = comparator.compare(10, 20)
    print(result)
    result = comparator.compare(30, 30)
    print(result)
    result = comparator.compare(50, 40)
    print(result)