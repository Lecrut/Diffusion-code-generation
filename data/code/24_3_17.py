def is_negative(x):
    return x < 0

if __name__ == '__main__':
    test_cases = [(-5, True), (0, False), (-1.5, True)]
    print("Testing negative check:")
    for val, expected in test_cases:
        result = is_negative(val)
        status = "PASS" if result == expected else "FAIL"
        print(f"x={val}: {result} ({status})")