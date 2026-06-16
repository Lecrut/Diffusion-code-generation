def sort_mixed_list(data):
    return sorted(
        [x if isinstance(x, (int, float)) else x for x in data], 
        key=lambda item: (isinstance(item, str), item)
    )
if __name__ == '__main__':
    sample_data = ["banana", 3.14, "apple", 2, "cherry", -5]
    sorted_result = sort_mixed_list(sample_data)
    print(sorted_result)