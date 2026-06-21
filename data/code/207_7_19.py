def flatten_and_find_max(nested_list):
    if not nested_list:
        return None
    
    flat_list = []
    
    def flatten(sublist):
        for item in sublist:
            if isinstance(item, list):
                flatten(item)
            else:
                flat_list.append(item)
    
    flatten(nested_list)
    return max(flat_list)

if __name__ == '__main__':
    sample_list1 = [3, 5, [2, 8], [9, [1, 7]]]
    result1 = flatten_and_find_max(sample_list1)
    print(f"List: {sample_list1}, Max: {result1}")
    
    sample_list2 = [[4, 6], 3, 10]
    result2 = flatten_and_find_max(sample_list2)
    print(f"List: {sample_list2}, Max: {result2}")
    
    sample_list3 = [7, [5, [8]], [3, 2]]
    result3 = flatten_and_find_max(sample_list3)
    print(f"List: {sample_list3}, Max: {result3}")