def test_conditional_expressions(value):
    if value > 0:
        result = "Positive"
    elif value < 0:
        result = "Negative"
    else:
        result = "Zero"
    return result
if __name__ == '__main__':
    test_values = [10, -5, 0, 3.14, -100]
    print("Testing conditional expressions:")
    for val in test_values:
        output = test_conditional_expressions(val)
        print(f"Input: {val}, Output: {output}")