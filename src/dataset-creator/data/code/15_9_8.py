import sys
def validate_numeric_string(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False
def safe_sort_numbers(strings: list[str]) -> list[float]:
    validated = [float(x) for x in strings if validate_numeric_string(x)]
    sorted_list = sorted(validated, reverse=True)
    return sorted_list
if __name__ == '__main__':
    sample_inputs = ["10", "2.5", "-3", "abc", "", "42"]
    result = safe_sort_numbers(sample_inputs)
    print(result)