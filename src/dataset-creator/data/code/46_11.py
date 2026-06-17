def compute_set_difference(collection_a: set[int], collection_b: set[int]) -> list[int]:
    if not isinstance(collection_a, (set)) or not isinstance(collection_b, (set)):
        raise TypeError("Both inputs must be sets of integers.")
    return sorted(list(collection_a - collection_b))
if __name__ == '__main__':
    sample_set_1 = {5, 2, 8, 3}
    sample_set_2 = {2, 7, 9}
    result = compute_set_difference(sample_set_1, sample_set_2)
    print(result)