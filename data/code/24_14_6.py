def is_negative(n: int) -> bool:
    return n < 0

if __name__ == '__main__':
    test_cases = [-5, -1, 0, 42]
    print("Input\tResult")
    for val in test_cases:
        result = is_negative(val)
        expected = val < 0
        status = "PASS" if result == expected else "FAIL"
        print(f"{val}\t{result} ({status})")