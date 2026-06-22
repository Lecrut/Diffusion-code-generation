class ValueComparator:

    def compare(self, val1, val2):
        comparison_result = {(True, False): f'{val1} is greater than {val2}', (False, True): f'{val1} is less than {val2}', (False, False): f'{val1} is equal to {val2}'}
        return comparison_result.get((val1 > val2, val1 < val2), 'Values are not comparable')
if __name__ == '__main__':
    comparator = ValueComparator()
    result1 = comparator.compare(10, 20)
    print(result1)
    result2 = comparator.compare(30, 15)
    print(result2)
    result3 = comparator.compare(7, 7)
    print(result3)