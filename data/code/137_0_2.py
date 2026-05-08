def test_conditional_expressions():
    value = 7
    if value > 10:
        result = "Greater than 10"
    elif value >= 5:
        result = "Between 5 and 10 (inclusive)"
    else:
        result = "Less than 5"
    print(f"Testing value: {value}")
    print(f"Result: {result}")
    value = 3
    if value > 10:
        result = "Greater than 10"
    elif value >= 5:
        result = "Between 5 and 10 (inclusive)"
    else:
        result = "Less than 5"
    print(f"Testing value: {value}")
    print(f"Result: {result}")
    value = 10
    if value > 10:
        result = "Greater than 10"
    elif value >= 5:
        result = "Between 5 and 10 (inclusive)"
    else:
        result = "Less than 5"
    print(f"Testing value: {value}")
    print(f"Result: {result}")
if __name__ == '__main__':
    test_conditional_expressions()