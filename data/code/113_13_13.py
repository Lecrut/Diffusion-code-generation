def subtract_integers(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return a - b

if __name__ == '__main__':
    sample_values = {
        "num1": 20,
        "num2": 7
    }
    result = subtract_integers(sample_values["num1"], sample_values["num2"])
    print(result)