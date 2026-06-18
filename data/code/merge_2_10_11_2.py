import timeit
def sort_dict_by_value_length(data: dict) -> list[tuple[str, int]]:
    return sorted(
        data.items(), key=lambda item: len(str(item[1]))
    )
if __name__ == '__main__':
    sample_data = {
        'apple': 50,
        'banana': 2.718,
        'cherry': [1, 2, 3],
        'date': {'nested': True},
        'elderberry': "a" * 1000,
    }
    start = timeit.default_timer()
    result = sort_dict_by_value_length(sample_data)
    end = timeit.default_timer()
    print("Sorted items:")
    for key, val in result:
        print(f"{key}: {val}")
    print(f"Time taken (single run): {end - start:.6f} seconds")