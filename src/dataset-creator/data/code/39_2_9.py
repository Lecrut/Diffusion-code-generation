class InvalidTypeException(Exception):
    pass
def find_largest_element(numbers):
    if not numbers:
        raise ValueError("List is empty")
    for i in range(len(numbers)):
        val = numbers[i]
        try:
            float(val)
        except (ValueError, TypeError):
            raise InvalidTypeException(f"Invalid entry at index {i}: '{val}'")
    return max(float(x) for x in numbers)
if __name__ == '__main__':
    sample_list = [10.5, 20, "30", -5, None]
    try:
        result = find_largest_element(sample_list)
        print(f"Largest element is {result}")
    except InvalidTypeException as e:
        print(f"Error encountered: {e}")