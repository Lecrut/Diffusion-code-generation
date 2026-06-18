import math
def is_even_mathematical_property(n: int) -> bool:
    return n & 1 == 0
if __name__ == '__main__':
    test_cases = [42, -37, 0, 1]
    results = []
    for val in test_cases:
        result = is_even_mathematical_property(val)
        results.append(f"{val}: {result}")
    print("\n".join(results))