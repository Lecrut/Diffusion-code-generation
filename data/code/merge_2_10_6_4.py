def sort_mixed_list(data):
    def get_sort_key(item):
        if isinstance(item, (int, float)):
            return item
        elif isinstance(item, str):
            return ('0', item.lower())                                                    
        else:
            return (1, str(item))
    sorted_data = sorted(data, key=get_sort_key)
    if __name__ == '__main__':
        sample_list = [3.5, "apple", 42, -10, "banana", 3.14, "cherry"]
        print("Original list:", sample_list)
        sorted_result = sort_mixed_list(sample_list)
        print("Sorted result:", sorted_result)