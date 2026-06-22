class QuantityComparator:
    MESSAGE_GREATER = 'is greater'
    MESSAGE_LESS = 'is less'
    MESSAGE_EQUAL = 'are equal'

    @staticmethod
    def compare_two_simple_quantities_now_calculate(quantity1, quantity2):
        if not isinstance(quantity1, (int, float)) or not isinstance(quantity2, (int, float)):
            raise ValueError("Both inputs must be numbers")
        if quantity1 > quantity2:
            return f'Quantity 1 {QuantityComparator.MESSAGE_GREATER}'
        elif quantity1 < quantity2:
            return f'Quantity 2 {QuantityComparator.MESSAGE_LESS}'
        else:
            return f'Quantities {QuantityComparator.MESSAGE_EQUAL}'

if __name__ == '__main__':
    result = QuantityComparator.compare_two_simple_quantities_now_calculate(10, 20)
    print(result)