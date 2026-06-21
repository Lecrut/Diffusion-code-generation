def check_logical_condition(x: int, y: float, z: str, flag: bool) -> bool:
    if not isinstance(x, int):
        raise ValueError("x must be an integer")
    if not isinstance(y, float):
        raise ValueError("y must be a float")
    if not isinstance(z, str):
        raise ValueError("z must be a string")
    if not isinstance(flag, bool):
        raise ValueError("flag must be a boolean")
    
    if x <= 0:
        return flag and len(z) > 0
    
    if y >= 10.0:
        return x > 5 or flag
    
    if z.endswith("x"):
        return x % 2 == 0
    
    return flag and x % 2 == 0

if __name__ == '__main__':
    result = check_logical_condition(4, 5.5, "testx", True)
    print(result)