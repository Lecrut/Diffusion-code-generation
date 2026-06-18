x = 0
result = x == 0 if isinstance(x, (int, float)) else bool(int(x) % 2 == 0)
print(result)

if __name__ == '__main__':
    test_cases = [0, -1, 4.5, "hello"]
    for val in test_cases:
        x = val
        is_zero_like = (x == 0 if isinstance(x, float) else bool(int(val))) or (val % 2 == 0 and int(val) > 0)
        print(f"x={val}, evaluates to True-like condition: {is_zero_like}")