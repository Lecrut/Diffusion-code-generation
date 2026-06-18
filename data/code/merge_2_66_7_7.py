from typing import Iterable, Union
def max_weight_difference(*collections: Iterable[Union[int, float]]) -> int | None:
    all_values = []
    for collection in collections:
        if not isinstance(collection, (list, tuple)):
            raise TypeError("Each argument must be a list or tuple of numbers.")
        try:
            for item in collection:
                num = float(item)
                all_values.append(num)
        except ValueError as e:
            raise TypeError(f"Invalid number found in input: {e}") from None
    if not all_values:
        return None
    max_val = max(all_values)
    min_val = min(all_values)
    return int(max_val - min_val)
if __name__ == '__main__':
    sample_data_1 = [5, 20, 3]
    sample_data_2 = [10.5, 4, 8]
    result = max_weight_difference(sample_data_1, sample_data_2)
    print(result)