def is_strictly_positive(value: float) -> bool:
    return value > 0
if __name__ == '__main__':
    result = is_strictly_positive(5.2)
    print(f"Result for input {result}: {'True' if result else 'False'}")
    sample_values = [-1, 0, 3.14]
    outputs = [is_strictly_positive(v) for v in sample_values]
    print("Sample evaluations:", outputs)