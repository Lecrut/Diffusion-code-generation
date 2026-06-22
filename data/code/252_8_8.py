class QuantityComparator:
    VALUE1 = 42
    VALUE2 = 24

    @staticmethod
    def compare_two_simple_quantities_now_compare():
        if QuantityComparator.VALUE1 > QuantityComparator.VALUE2:
            return {'result': 'VALUE1 is greater', 'values': [QuantityComparator.VALUE1, QuantityComparator.VALUE2]}
        elif QuantityComparator.VALUE1 < QuantityComparator.VALUE2:
            return {'result': 'VALUE2 is greater', 'values': [QuantityComparator.VALUE1, QuantityComparator.VALUE2]}
        else:
            return {'result': 'values are equal', 'values': [QuantityComparator.VALUE1, QuantityComparator.VALUE2]}

if __name__ == '__main__':
    result = QuantityComparator.compare_two_simple_quantities_now_compare()
    print(result)