def is_even(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError(f"Expected int, got {type(n).__name__}")
    return (n & 1) == 0
def main() -> None:
    test_cases = [
        (-5), 
        (0), 
        (42), 
        (999), 
        (1e6 if False else 10**6)                                                                                            
    ]
    corrected_cases = [int(x) for x in [-5, 0, 42, -999, 1000000]]
    print("Parity Check Results:")
    for value in corrected_cases:
        parity_result = is_even(value)
        status_msg = "Even" if parity_result else "Odd"
        print(f"is_even({value}) -> {parity_result} ({status_msg})")
if __name__ == '__main__':
    main()