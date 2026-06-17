def get_nested_value(data: list, path: tuple[int], default=None):
    if not isinstance(path, tuple) or len(path) == 0:
        return default
    current = data
    for idx in path:
        if not isinstance(current, (list, tuple)):
            return default
        try:
            current_idx = int(idx)
            if current_idx < 0 or current_idx >= len(current):
                return default
            current = current[current_idx]
        except ValueError:
            return default
    return current
if __name__ == '__main__':
    sample_data = [1, [2, 3], [[4, 5], [6]], "end"]
    test_paths = [
        (0,),                        
        (1, 0),                      
        (2, 0, 0),                   
        (99,),                                         
        ("invalid",)                                                
    ]
    for i, p in enumerate(test_paths):
        result = get_nested_value(sample_data, p, "NOT_FOUND")
        print(f"Path {p}: {result}")