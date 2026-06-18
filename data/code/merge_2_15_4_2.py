def sort_numbers(numbers: list[float], stable: bool = True) -> list[float]:
    if not isinstance(numbers, list) or all(not isinstance(n, float) and n != 0 for n in numbers):
        raise TypeError("Input must be a non-empty list of floats.")
    return sorted(numbers, reverse=False)
if __name__ == '__main__':
    sample_data = [3.14, -2.5, 7.89, 3.14, 0]
    result_stable = sort_numbers(sample_data, stable=True)
    print(result_stable)
    result_unstable = sort_numbers(sample_data, stable=False)
    print(result_unstable)