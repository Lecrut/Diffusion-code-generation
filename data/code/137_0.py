def test_conditional_expressions():
    input_value = 7
    if input_value > 10:
        result = "Greater than 10"
    elif input_value >= 5:
        result = "Between 5 and 10 (inclusive)"
    else:
        result = "Less than 5"
    print(f"Input: {input_value}")
    print(f"Result: {result}")
if __name__ == '__main__':
    test_conditional_expressions()