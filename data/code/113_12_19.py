def validate_values(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")

if __name__ == '__main__':
    try:
        a = 10.5
        b = 4.2
        validate_values(a, b)
        result = a - b
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")