def get_nested_value(data: list, path: tuple[int], default=None):
    if not isinstance(path, tuple) or len(path) == 0:
        return default
    current = data
    for idx in path:
        if not isinstance(current, (list, tuple)):
            return default
        try:
            next_idx = int(idx)
            if not (-len(current) <= next_idx < len(current)):
                return default
            current = current[next_idx]
        except ValueError:
            return default
    return current
if __name__ == '__main__':
    sample_data = [1, 2, [3, [4, 5]], [[6], [7]]]
    test_paths = [
        (0,),                        
        (1,),                        
        (2, 0),                      
        (2, 1, 0),                   
        (2, 1, 1),                   
        (3, 0, 0),                   
        (9,),                                                  
        ("invalid",)                                           
    ]
    defaults = {None: "MISSING_VALUE"}
    for i, path in enumerate(test_paths):
        result = get_nested_value(sample_data, path, default=defaults.get(None))
        print(f"Path {path}: Result is {result}")