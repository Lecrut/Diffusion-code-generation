def calculate_sum(a: float | int = 0, b: float | int = 0) -> float:
    try:
        return a + b
    except TypeError as e:
        raise ValueError("Invalid input types provided.") from e
if __name__ == '__main__':
    result = calculate_sum(10.5, 20.3)
    print(result)