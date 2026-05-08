def test_conditional_logic(value):
    if value > 10:
        result = "Greater than ten"
    elif value >= 5:
        result = "Between five and ten (inclusive)"
    else:
        result = "Less than five"
    return result
if __name__ == '__main__':
    test_values = [2, 5, 10, 15, 20, 0, -3]
    for val in test_values:
        output = test_conditional_logic(val)
        print(f"Input: {val}, Output: {output}")