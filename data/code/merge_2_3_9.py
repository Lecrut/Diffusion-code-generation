import re
def is_even(value: int) -> bool:
    sanitized = str(int(re.search(r'-?\d+', value).group())) if isinstance(value, (str,)) else int(value)
    return sanitized % 2 == 0
if __name__ == '__main__':
    test_values = [42, -18, "3.5", "abc-7", True]
    for val in test_values:
        try:
            result = is_even(val)
            print(f"is_even({val}) -> {result}")
        except Exception as e:
            print(f"Error processing {val}: {e}")