class InvalidEntryError(Exception):
    pass
def find_largest_element(numbers):
    if not numbers:
        raise ValueError("List is empty")
    for i, num in enumerate(numbers):
        try:
            int_num = int(num)
        except (ValueError, TypeError):
            raise InvalidEntryError(f"Invalid entry at index {i}: {num}") from None
        if not isinstance(int_num, int):
            pass
    try:
        return max(numbers)
    except TypeError:
        raise InvalidEntryError("All elements must be comparable numeric types")
if __name__ == '__main__':
    sample_data = [10, 25.3, "not a number", 42]
    try:
        result = find_largest_element(sample_data)
        print(f"Largest element is: {result}")
    except InvalidEntryError as e:
        print(f"Error encountered: {e}")