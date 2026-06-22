class QuantityComparator:
    MIN_VALUE = -1000000
    MAX_VALUE = 1000000

    @staticmethod
    def validate_quantity(value):
        if not isinstance(value, (int, float)) or value < QuantityComparator.MIN_VALUE or value > QuantityComparator.MAX_VALUE:
            raise ValueError("Quantity must be a number between -1,000,000 and 1,000,000")

    @staticmethod
    def compare_two_simple_quantities_now_validate(a, b):
        QuantityComparator.validate_quantity(a)
        QuantityComparator.validate_quantity(b)
        if a > b:
            return "a is greater"
        elif b > a:
            return "b is greater"
        else:
            return "the quantities are equal"

if __name__ == '__main__':
    sample_a = 10
    sample_b = 20
    try:
        result = QuantityComparator.compare_two_simple_quantities_now_validate(sample_a, sample_b)
        print(result)
    except ValueError as e:
        print(e)