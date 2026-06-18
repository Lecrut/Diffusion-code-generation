def sort_mixed_list(data):
    return sorted(
        [x if isinstance(x, (int, float)) else 0 for x in data], 
        key=lambda x: x if isinstance(x, (int, float)) else 1e9
    )
if __name__ == '__main__':
    sample_data = [3.5, "apple", 7, None, "banana", -2, [], True]
    sorted_result = sort_mixed_list(sample_data)
    print(sorted_result)