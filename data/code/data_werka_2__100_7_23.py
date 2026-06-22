def check_logical_state(x: int, y: str, z: float) -> bool:
    if not isinstance(x, int):
        raise ValueError("x must be an integer")
    if not isinstance(y, str):
        raise ValueError("y must be a string")
    if not isinstance(z, float):
        raise ValueError("z must be a float")
    
    if x < 0:
        return False
    
    is_valid_string = len(y) > 0 and y.isalnum()
    
    if z > 50.0:
        return is_valid_string
    
    if z > 10.0:
        return x > 5
    
    return is_valid_string and x > 0

if __name__ == '__main__':
    result = check_logical_state(10, "abc123", 25.5)
    print(result)