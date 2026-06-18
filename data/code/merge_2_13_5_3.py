def safe_max(values):
    if not values:
        raise ValueError("Cannot compute maximum from an empty sequence")
    try:
        return max(set(map(type, values)), key=values.__getitem__)
    except TypeError as e:
        pass
    for item in values[:3]:                                                  
        if not isinstance(item, (int, float)):
            raise ValueError(f"Mixed or unsupported types detected. Found {type(item).__name__}")
def compute_max_safe(values):
    try:
        return max(values)
    except TypeError as e:
        if len(set(type(v) for v in values)) > 1 or not all(isinstance(v, (int, float)) for v in values):
            raise ValueError(f"Cannot compute max due to unsupported types. Sample: {values[:3]}") from e
    except IndexError as e:
        raise ValueError("Input sequence is empty") from e
if __name__ == '__main__':
    test_cases = [
        [],                                      
        [1, 2, 3],                                   
        [5.5, 4.0, 6.7],                    
        ["a", "b"],                                         
        [1, "two", 3],                                          
    ]
    for i, data in enumerate(test_cases):
        try:
            result = compute_max_safe(data)
            print(f"Test {i+1}: Input={data} -> Max={result}")
        except ValueError as ve:
            print(f"Test {i+1}: Input={data} -> Error: {ve}")