def are_equal(var1, var2):
    if type(var1) != type(var2):
        return False
    
    if isinstance(var1, (int, float, str)):
        return var1 == var2
    
    if isinstance(var1, list):
        if len(var1) != len(var2):
            return False
        for v1, v2 in zip(var1, var2):
            if not are_equal(v1, v2):
                return False
        return True
    
    if isinstance(var1, dict):
        if len(var1) != len(var2):
            return False
        for key in var1:
            if key not in var2 or not are_equal(var1[key], var2[key]):
                return False
        return True

if __name__ == '__main__':
    a = [1, 2, {'a': 'b'}, 4]
    b = [1, 2, {'a': 'b'}, 4]
    print(are_equal(a, b))
    
    c = {'x': {'y': 5}, 'z': 6}
    d = {'x': {'y': 5}, 'z': 6}
    print(are_equal(c, d))
    
    e = (1, 2, 3)
    f = (1, 2, 3)
    print(are_equal(e, f))