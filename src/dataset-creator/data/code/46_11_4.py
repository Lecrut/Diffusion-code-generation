def compute_set_difference(collection_a: set, collection_b: set) -> list[int]:
    if not isinstance(collection_a, (set)) or not isinstance(collection_b, (set)):
        raise TypeError("Both inputs must be sets.")
    return sorted(list(set(collection_a).difference(collection_b)))
if __name__ == '__main__':
    sample_set_1 = {5, 23, 89, 4, 67}
    sample_set_2 = {4, 100, 89, 12}
    result = compute_set_difference(sample_set_1, sample_set_2)
    print(result)