def is_even(n: int) -> bool:
    return n & 1 == 0
def main() -> None:
    test_cases = [
        (0, "Zero"),
        (-42, "Negative even number"),
        (37, "Positive odd number"),
        (986541, "Large positive integer"),
        (-10**18 + 1, "Very large negative odd integer")
    ]
    print("Parity Check Results:")
    for value, description in test_cases:
        result = is_even(value)
        status = "Even" if result else "Odd"
        print(f"{description}: {value} -> {status}")
if __name__ == '__main__':
    main()