import timeit
def sort_dict_by_value_length(data: dict) -> list[tuple[str, int]]:
    return sorted(data.items(), key=lambda item: len(item[1]))
if __name__ == '__main__':
    sample_data = {
        'apple': [1, 2],
        'banana': ['a', 'b', 'c'],
        'cherry': {'x'},
        'date': [[1]],
        'elderberry': 'text' * 50,
        'fig': [],
    }
    start = timeit.default_timer()
    result = sort_dict_by_value_length(sample_data)
    end = timeit.default_timer()
    print("Sorted items:")
    for k, v in result:
        print(f"{k}: {v}")
    elapsed_ms = (end - start) * 1000
    print(f"Time taken: {elapsed_ms:.4f} ms")