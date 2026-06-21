def intersect(*lists):
    if not all(isinstance(lst, list) for lst in lists):
        raise ValueError("All arguments must be lists")
    
    sets = [set(lst) for lst in lists]
    common_elements = set.intersection(*sets)
    return sorted(list(common_elements))

if __name__ == '__main__':
    sample_lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    result = intersect(*sample_lists)
    print(result)