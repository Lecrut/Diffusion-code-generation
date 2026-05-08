def test_conditional_expressions(value):
    if value > 10:
        result = "Greater than ten"
    elif value >= 5:
        result = "Between five and ten (inclusive)"
    else:
        result = "Less than five"
    return result
if __name__ == '__main__':
    sample_inputs = [2, 5, 10, 15, 20, 0, -3]
    for number in sample_inputs:
        output = test_conditional_expressions(number)
        print(f"Input: {number}, Output: {output}")