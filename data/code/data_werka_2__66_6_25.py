class NumberComparator:
    NUMERIC_TYPES = (int, float)

    @staticmethod
    def is_numeric(value):
        return isinstance(value, NumberComparator.NUMERIC_TYPES)

    @staticmethod
    def compare_adjacent_numbers(elements):
        for i in range(len(elements) - 1):
            if not (NumberComparator.is_numeric(elements[i]) and NumberComparator.is_numeric(elements[i + 1])):
                raise TypeError(f"Non-numeric adjacent elements found: {elements[i]} and {elements[i + 1]}")

if __name__ == '__main__':
    sample_values = [3, 4.5, 'hello', 7, 8]
    try:
        NumberComparator.compare_adjacent_numbers(sample_values)
    except TypeError as e:
        print(e)