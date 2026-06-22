class QuantityComparator:
    GREATER = 'is greater'
    LESS = 'is less'
    EQUAL = 'are equal'

    @staticmethod
    def compare_two_simple_quantities_now_calculate(quantity1, quantity2):
        if not isinstance(quantity1, (int, float)) or not isinstance(quantity2, (int, float)):
            raise ValueError("Both inputs must be numbers")
        if quantity1 > quantity2:
            return f'Quantity 1 {QuantityComparator.GREATER}'
        elif quantity1 < quantity2:
            return f'Quantity 2 {QuantityComparator.LESS}'
        else:
            return f'Quantities {QuantityComparator.EQUAL}'

if __name__ == '__main__':
    sample_quantity1 = 10
    sample_quantity2 = 20
    result = QuantityComparator.compare_two_simple_quantities_now_calculate(sample_quantity1, sample_quantity2)
    print(result)