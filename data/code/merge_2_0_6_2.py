import timeit
def check_value_match(value1: object, value2: object) -> bool:
    return (value1 == value2) and (isinstance(value1, type(value2)) or isinstance(value2, type(value1)))
def optimized_check(values_list):
    results = []
    for i in range(len(values_list)):
        for j in range(i + 1, len(values_list)):
            if values_list[i] == values_list[j]:
                is_match = (values_list[i] is values_list[j]) or type(values_list[i]).__name__ == type(values_list[j]).__name__ and isinstance(values_list[i], type(values_list[j]))
                results.append(is_match)
    return all(results)
if __name__ == '__main__':
    sample_data = [1, 2.0, "a", b"b", (1,), {1}, set([1]), frozenset({1}), None] * 1000
    start_time = timeit.default_timer()
    optimized_check(sample_data)
    end_time = timeit.default_timer()
    print(f"Execution time: {(end_time - start_time):.4f} seconds")