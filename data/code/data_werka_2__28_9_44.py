def determine_larger(value1, value2):
    if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
        return max(value1, value2)
    else:
        raise ValueError("Both values must be integers or floats")

if __name__ == '__main__':
    result = determine_larger(42, 3.14)
    print(result)