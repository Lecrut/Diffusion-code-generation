def count_items(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    sample_data = [0, 1, 2, 3]
    empty_list = []
    result_full = count_items(sample_data)
    result_empty = count_items(empty_list)
    print(f"Count for {sample_data}: {result_full}")
    print(f"Count for {empty_list}: {result_empty}")