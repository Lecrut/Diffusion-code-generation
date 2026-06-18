import sys
def validate_numeric_string(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False
def safe_sort_numbers(strings: list[str]) -> None:
    validated = [s for s in strings if validate_numeric_string(s)]
    sorted_list = sorted(validated, key=float)
    print(", ".join(sorted_list))
if __name__ == '__main__':
    sample_inputs = ["123", "45.67", "-890", "abc", "", "  ", "0"]
    safe_sort_numbers(sample_inputs)