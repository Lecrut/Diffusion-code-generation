def decimal_to_binary_string(number: int) -> str:
    if number < 0:
        raise ValueError("Only positive decimal integers are accepted.")
    if number == 0:
        return "0b0"
    return f"{number:b}"

if __name__ == "__main__":
    test_values = [0, 5, 10, 255, 1024]
    for value in test_values:
        result = decimal_to_binary_string(value)
        print(result)