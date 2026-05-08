def test_conditional_expressions(value):
    if value > 0:
        result = "Positive"
    elif value < 0:
        result = "Negative"
    else:
        result = "Zero"
    return result
sample_inputs = [10, -5, 0, 3.14, -100]
for input_value in sample_inputs:
    output = test_conditional_expressions(input_value)
    print(f"Input: {input_value}, Output: {output}")
if __name__ == '__main__':
    pass