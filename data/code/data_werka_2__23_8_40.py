class ValueComparator:

    def compare_values(self, val1, val2):
        if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
            return (val1 > val2, val1 < val2, val1 == val2)
        elif isinstance(val1, str) and isinstance(val2, str):
            return (val1 > val2, val1 < val2, val1 == val2)
        else:
            raise ValueError('Unsupported input types for comparison')
if __name__ == '__main__':
    comparator = ValueComparator()
    result_numeric = comparator.compare_values(10, 20)
    print(result_numeric)
    result_string = comparator.compare_values('apple', 'banana')
    print(result_string)