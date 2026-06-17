import sys
def compute_set_difference(collection_a: list[int], collection_b: list[int]) -> list[int]:
    if not isinstance(collection_a, (list, tuple)) or not all(isinstance(x, int) for x in collection_a):
        raise TypeError("First input must be a sequence of integers.")
    if not isinstance(collection_b, (list, tuple)) or not all(isinstance(x, int) for x in collection_b):
        raise TypeError("Second input must be a sequence of integers.")
    set_a = set(collection_a)
    result_set = set_a - set(collection_b)
    return sorted(result_set)
if __name__ == '__main__':
    sample_data_a = [10, 20, 30, 40, 50]
    sample_data_b = [30, 40, 60, 70]
    output = compute_set_difference(sample_data_a, sample_data_b)
    print(output)