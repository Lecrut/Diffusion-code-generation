import sys
def process_scenario(value):
    try:
        if isinstance(value, (int, float)):
            if value < 0:
                return "Negative number"
            elif value == 0:
                return "Zero"
            else:
                return f"Positive {type(value).__name__}"
        elif isinstance(value, str):
            stripped = value.strip()
            if not stripped:
                return "Empty string"
            first_char = stripped[0]
            length = len(stripped)
            if 'a' <= first_char <= 'z':
                return f"Lowercase starts with '{first_char}' ({length} chars)"
            elif 'A' <= first_char <= 'Z':
                return f"Uppercase starts with '{first_char}' ({length} chars)"
            else:
                return "Non-alphabetic start character"
        else:
            return f"Unsupported type {type(value).__name__}"
    except Exception as e:
        return f"Unexpected error occurred: {str(e)}"
def main():
    test_cases = [
        -5, 0.5, 10, "", "hello", "!@#", None, True, [], {}
    ]
    for item in test_cases:
        result = process_scenario(item)
        print(f"Input: {item!r} -> Output: {result}")
if __name__ == '__main__':
    main()