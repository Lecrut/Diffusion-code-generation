def repeat_pattern(base_pattern: str, multiplier: int) -> str:
    if multiplier <= 0:
        return ""
    return base_pattern * multiplier
if __name__ == '__main__':
    pattern1 = "abc"
    multiplier1 = 3
    result1 = repeat_pattern(pattern1, multiplier1)
    print(f"Pattern: '{pattern1}', Multiplier: {multiplier1}, Result: '{result1}'")
    pattern2 = "hello"
    multiplier2 = 2
    result2 = repeat_pattern(pattern2, multiplier2)
    print(f"Pattern: '{pattern2}', Multiplier: {multiplier2}, Result: '{result2}'")
    pattern3 = "xyz"
    multiplier3 = 5
    result3 = repeat_pattern(pattern3, multiplier3)
    print(f"Pattern: '{pattern3}', Multiplier: {multiplier3}, Result: '{result3}'")
    pattern4 = "a"
    multiplier4 = 0
    result4 = repeat_pattern(pattern4, multiplier4)
    print(f"Pattern: '{pattern4}', Multiplier: {multiplier4}, Result: '{result4}'")