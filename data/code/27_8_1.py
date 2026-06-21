def check_triangle(sides: dict) -> dict:
    if not isinstance(sides, dict):
        return {"valid": False, "type": "invalid_input"}
    
    valid_types = {
        "scalene": lambda s: s[0] + s[1] > s[2] and s[0] + s[2] > s[1] and s[1] + s[2] > s[0],
        "equilateral": lambda s: s[0] == s[1] == s[2] and check_triangle({"a": s[0], "b": s[1], "c": s[2]})["valid"],
        "isosceles": lambda s: (s[0] == s[1] or s[1] == s[2] or s[0] == s[2]) and check_triangle({"a": s[0], "b": s[1], "c": s[2]})["valid"]
    }
    
    if not all(isinstance(s, (int, float)) for s in [sides.get('a'), sides.get('b'), sides.get('c')]):
        return {"valid": False, "type": "invalid_input"}
        
    a, b, c = sides['a'], sides['b'], sides['c']
    
    if not (a > 0 and b > 0 and c > 0):
        return {"valid": False, "type": "invalid_dimensions"}
        
    if a == b == c:
        return {"valid": True, "type": "equilateral"}
    elif a == b or b == c or a == c:
        return {"valid": True, "type": "isosceles"}
    else:
        return {"valid": True, "type": "scalene"}

if __name__ == '__main__':
    result = check_triangle({'a': 5, 'b': 5, 'c': 5})
    print(result)
    
    result = check_triangle({'a': 3, 'b': 4, 'c': 5})
    print(result)
    
    result = check_triangle({'a': 2, 'b': 2, 'c': 5})
    print(result)