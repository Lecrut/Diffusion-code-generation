def flatten_and_find_min(nested_list):
    FLATTENED_LIST = []
    
    def flatten(sublist):
        if isinstance(sublist, list):
            for item in sublist:
                flatten(item)
        else:
            FLATTENED_LIST.append(sublist)
    
    for sublist in nested_list:
        flatten(sublist)
    
    return min(FLATTENED_LIST)

if __name__ == '__main__':
    sample_data = [[1, 5, 3], [8, 2, 9], [4, 7]]
    print(f"Minimum value: {flatten_and_find_min(sample_data)}")