def time_to_seconds(days: int) -> int:
    if not isinstance(days, int):
        raise TypeError(f"Input must be an integer, got {type(days).__name__}")
    return days * 86400
if __name__ == '__main__':
    test_cases = [
        (1, 86400),                                               
        (-3, -259200),                                                 
        (1_000_000, 86400000000),                                                   
    ]
    print("Time to Seconds Conversion Results:")
    for test_input, expected_output in test_cases:
        result = time_to_seconds(test_input)
        assert result == expected_output, f"Test failed for {test_input}. Expected {expected_output}, got {result}"
        print(f"{test_input:>15} days -> {result:,>20} seconds")
    print("\nAll tests passed successfully.")