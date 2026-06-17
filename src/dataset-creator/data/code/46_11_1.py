def compute_set_difference(collection_a: set[int], collection_b: set[int]) -> list[int]:
    if not isinstance(collection_a, (set)) or not isinstance(collection_b, (set)):
        raise TypeError("Both inputs must be sets of integers.")
    return sorted(list(set(collection_a) - collection_b))
if __name__ == '__main__':
    sample_set_1 = {5, 23, 47, 89, 10}
    sample_set_2 = {23, 67, 89, 12}
    result = compute_set_difference(sample_set_1, sample_set_2)
    print(result)