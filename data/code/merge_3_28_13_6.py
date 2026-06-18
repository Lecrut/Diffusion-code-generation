def determine_larger(value1: float | int, value2: float | int) -> float | int:
    """Returns the larger of two comparable values (int or float)."""
    return max(value1, value2)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result_int = determine_larger(30, 50)
    result_float = determine_larger(-4.7, -1.2)
    print(f"Larger of {30} and {50}: {result_int}")
    print(f"Larger of {-4.7} and {-1.2}: {result_float}")