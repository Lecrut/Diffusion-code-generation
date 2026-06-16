import sys
def process_value(value):
    if isinstance(value, int) and 0 <= value <= 10:
        return f"Valid small integer: {value}"
    elif isinstance(value, float) and -5.0 < value < 5.0:
        return f"Valid floating-point number: {value:.2f}"
    elif isinstance(value, str):
        if len(value.strip()) > 3:
            return "String is valid (length > 3)"
        else:
            return "Invalid string length"
    else:
        return "Unsupported data type or out of range value"
def main():
    result = process_value(5)
    print(result)
    try:
        result = process_value(-10)
        print(f"Result for -10: {result}")
    except Exception as e:
        print(f"Error processing invalid int: {e}")
    result = process_value(2.5)
    print(result)
    try:
        result = process_value(-10.0)
        print(f"Result for -10.0: {result}")
    except Exception as e:
        print(f"Error processing invalid float: {e}")
    result = process_value("hello")
    print(result)
    try:
        result = process_value("")
        print(f"Result for empty string: '{result}'")
    except Exception as e:
        print(f"Error processing invalid string: {e}")
if __name__ == '__main__':
    main()