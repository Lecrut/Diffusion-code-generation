import sys
def safe_sort_numeric_strings(strings: list[str]) -> list[int]:
    validated = []
    for s in strings:
        try:
            num = int(s) if '.' not in s else float(s)
            rounded_num = round(num)
            validated.append(rounded_num)
        except ValueError:
            continue
    return sorted(validated, reverse=True)
if __name__ == '__main__':
    sample_input = ["123", "45.67", "-890", "abc", "", "+10"]
    result = safe_sort_numeric_strings(sample_input)
    print(result)