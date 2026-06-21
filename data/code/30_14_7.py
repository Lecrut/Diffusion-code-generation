def decimal_to_binary(n: int) -> str:
    return f"{n:b}"

if __name__ == "__main__":
    sample_value = 42
    result = decimal_to_binary(sample_value)
    print(result)