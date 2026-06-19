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
    result1 = comparator.compare(10, 5)
    result2 = comparator.compare(3.5, 4.2)
    result3 = comparator.compare("apple", "banana")
    
    print(result1)
    print(result2)
    print(result3)