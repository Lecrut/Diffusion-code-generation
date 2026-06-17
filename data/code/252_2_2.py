class QuantityComparer:
    def compare(self, a: int, b: int) -> dict:
        result = {}
        if a > b:
            result['comparison'] = 'a is greater than b'
            result['difference'] = a - b
        elif a < b:
            result['comparison'] = 'a is less than b'
            result['difference'] = b - a
        else:
            result['comparison'] = 'a is equal to b'
            result['difference'] = 0
        return result
if __name__ == '__main__':
    comparer = QuantityComparer()
    value1 = 15
    value2 = 7
    comparison_result1 = comparer.compare(value1, value2)
    print(f"Comparing {value1} and {value2}: {comparison_result1}")
    value3 = 20
    value4 = 20
    comparison_result2 = comparer.compare(value3, value4)
    print(f"Comparing {value3} and {value4}: {comparison_result2}")
    value5 = 3
    value6 = 10
    comparison_result3 = comparer.compare(value5, value6)
    print(f"Comparing {value5} and {value6}: {comparison_result3}")