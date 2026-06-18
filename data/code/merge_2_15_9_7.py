import sys
def validate_numeric_string(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False
def safe_sort_numerics(strings: list[str]) -> list[float]:
    validated = [float(x) for x in strings if validate_numeric_string(x)]
    validated.sort()
    return validated
if __name__ == '__main__':
    sample_data = ["10", "3.5", "-2", "abc", "", "7"]
    result = safe_sort_numerics(sample_data)
    print(result)