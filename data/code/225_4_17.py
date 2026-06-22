def find_min_max(nested_list):
    if not nested_list:
        return None, None
    
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item
    
    flat_list = list(flatten(nested_list))
    
    if not flat_list:
        return None, None
    
    current_min = min(flat_list)
    current_max = max(flat_list)
    
    return current_min, current_max

if __name__ == '__main__':
    sample_data = [10, 5, [20, 3], [15, 25]]
    print(find_min_max(sample_data))