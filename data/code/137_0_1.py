def test_conditional_logic(value):
    if value > 0:
        result = "Positive"
    elif value == 0:
        result = "Zero"
    else:
        result = "Negative"
    return result
if __name__ == '__main__':
    sample_inputs = [10, -5, 0, 3.14, -100]
    print("Testing Conditional Expressions:")
    for num in sample_inputs:
        output = test_conditional_logic(num)
        print(f"Input: {num}, Output: {output}")