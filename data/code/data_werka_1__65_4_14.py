class ElementFetcher:
    def __init__(self, iterable):
        self.iterable = iterable

    @staticmethod
    def validate_position(position, length):
        if not isinstance(position, int):
            raise ValueError("Position must be an integer")
        if not (0 <= position < length):
            raise ValueError("Position is out of bounds")

    def get_element_at_position(self, position):
        self.validate_position(position, len(self.iterable))
        return self.iterable[position]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    fetcher = ElementFetcher(sample_list)
    valid_position = 2
    invalid_position_high = 4
    invalid_position_low = -1
    invalid_position_type = 1.5

    try:
        result_valid = fetcher.get_element_at_position(valid_position)
        print(f"Result for valid position {valid_position}: {result_valid}")
    except ValueError as e:
        print(f"Error for valid position: {e}")

    try:
        result_invalid_high = fetcher.get_element_at_position(invalid_position_high)
        print(f"Result for invalid high position {invalid_position_high}: {result_invalid_high}")
    except ValueError as e:
        print(f"Error for invalid high position: {e}")

    try:
        result_invalid_low = fetcher.get_element_at_position(invalid_position_low)
        print(f"Result for invalid low position {invalid_position_low}: {result_invalid_low}")
    except ValueError as e:
        print(f"Error for invalid low position: {e}")

    try:
        result_invalid_type = fetcher.get_element_at_position(invalid_position_type)
        print(f"Result for invalid type position {invalid_position_type}: {result_invalid_type}")
    except ValueError as e:
        print(f"Error for invalid type position: {e}")