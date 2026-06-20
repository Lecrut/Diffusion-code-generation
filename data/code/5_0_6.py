def calculate_difference(length1: float, length2: float) -> float:
    return abs(length1 - length2)

if __name__ == '__main__':
    try:
        val1 = 15.5
        val2 = 7.2
        result = calculate_difference(val1, val2)
        print(result)
    except ValueError:
        print("Error: Invalid numeric input provided.")