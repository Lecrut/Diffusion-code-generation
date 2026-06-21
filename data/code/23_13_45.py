class ValueComparator:
    FIRST_VALUE_IS_GREATER = "First value is greater than the second value."
    FIRST_VALUE_IS_LESS = "First value is less than the second value."
    VALUES_ARE_EQUAL = "First value is equal to the second value."

    @staticmethod
    def compare(value1, value2):
        if value1 > value2:
            return ValueComparator.FIRST_VALUE_IS_GREATER
        elif value1 < value2:
            return ValueComparator.FIRST_VALUE_IS_LESS
        else:
            return ValueComparator.VALUES_ARE_EQUAL

if __name__ == '__main__':
    sample_value1 = 30
    sample_value2 = 45
    result = ValueComparator.compare(sample_value1, sample_value2)
    print(result)