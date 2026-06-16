import functools
def sort_numbers(numbers: list[int], stable: bool = True) -> list[int]:
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    comparison_key = lambda x: (-x,) if stable else -x
    return sorted(
        [int(x) for x in numbers], 
        key=functools.cmp_to_key(lambda a, b: (a > b) - (a < b)) if not stable else None
    )
if __name__ == '__main__':
    sample_data = [-5, 3, -10, 2.5]
    result_stable = sort_numbers(sample_data.copy(), stable=True)
    print(result_stable)
    result_unstable = sort_numbers(sample_data.copy(), stable=False)
    print(result_unstable)