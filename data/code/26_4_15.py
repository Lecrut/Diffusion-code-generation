# Optimized one-liner to check if x > y using comparison operators
result = (x := 10) > (y := 5)

if __name__ == '__main__':
    print(f"x is greater than y: {result}")
    # Additional verification with specific values
    sample_x, sample_y = 20.5, 30
    check_result = sample_x > sample_y
    assert check_result == False, "Assertion failed"