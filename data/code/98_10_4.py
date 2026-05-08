def test_multiple_conditions(a: bool, b: bool, c: bool) -> bool:
    return a and b and c
if __name__ == '__main__':
    condition1 = True
    condition2 = False
    condition3 = True
    result = test_multiple_conditions(condition1, condition2, condition3)
    print(f"Condition 1: {condition1}")
    print(f"Condition 2: {condition2}")
    print(f"Condition 3: {condition3}")
    print(f"Result of testing all conditions: {result}")