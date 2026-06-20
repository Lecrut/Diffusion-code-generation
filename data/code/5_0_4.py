def calculate_difference(length1, length2):
    try:
        value1 = float(length1)
        value2 = float(length2)
        return abs(value1 - value2)
    except (ValueError, TypeError):
        return None

if __name__ == '__main__':
    result1 = calculate_difference("10.5", "4.2")
    result2 = calculate_difference("5", "invalid")
    print(result1)
    print(result2)