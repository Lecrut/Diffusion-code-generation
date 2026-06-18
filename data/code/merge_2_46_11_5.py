import sys
def compute_set_difference(collection_a: list[int], collection_b: list[int]) -> list[int]:
    if not isinstance(collection_a, (list, tuple)) or not all(isinstance(x, int) for x in collection_a):
        raise TypeError("Collection A must be a sequence of integers.")
    if not isinstance(collection_b, (list, tuple)) or not all(isinstance(x, int) for x in collection_b):
        raise TypeError("Collection B must be a sequence of integers.")
    set_a = set(collection_a)
    result_set = set_a - set(collection_b)
    return sorted(result_set)
if __name__ == '__main__':
    sample_data_a = [10, 23, 45, 67, 89]
    sample_data_b = [23, 45, 78, 90]
    result = compute_set_difference(sample_data_a, sample_data_b)
    print(result)