def normalize_case_string(input_text: str) -> str:
    if len(input_text) == 0:
        return ""
    first_part = input_text[0:1].upper()
    remaining_part = input_text[1:].lower()
    return first_part + remaining_part

def process_sample(input_data: list) -> list:
    results = []
    for text in input_data:
        results.append(normalize_case_string(text))
    return results

if __name__ == '__main__':
    test_cases = ["hElLo", "WoRLD", "pyThOn", "a", "", "MiXeDcAsE", "123abc"]
    outputs = process_sample(test_cases)
    for idx, val in enumerate(outputs):
        print(f"{test_cases[idx]} -> {val}")