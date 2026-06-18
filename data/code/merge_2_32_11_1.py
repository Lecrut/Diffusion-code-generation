from typing import Any, Dict
def count_frequency(collection: list) -> dict[str, int]:
    frequency_map = {}
    for item in collection:
        try:
            if isinstance(item, (list, dict)):
                raise TypeError(f"Unhashable type '{type(item).__name__}' encountered.")
            current_count = frequency_map.get(item, 0) + 1
            frequency_map[item] = current_count
        except TypeError as e:
            raise
    return frequency_map
if __name__ == '__main__':
    sample_data = [10, 23, 'apple', 45, 'banana', 23, 'cherry']
    result = count_frequency(sample_data)
    print("Frequency counts:", result)