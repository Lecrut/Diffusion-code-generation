def test_conditional_expressions(value):
    if value > 0:
        result = "Positive"
    elif value < 0:
        result = "Negative"
    else:
        result = "Zero"
    return result
if __name__ == '__main__':
    sample_inputs = [10, -5, 0, 3.14, -100]
    print("Testing conditional expressions:")
    for num in sample_inputs:
        output = test_conditional_expressions(num)
        print(f"Input: {num}, Output: {output}")