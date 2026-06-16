def check_equality(a: any, b: any) -> bool:
    if type(a) is not type(b):
        return False
    identity_check = a is b
    try:
        hash_a = hash(a)
        hash_b = hash(b)
        value_equal = (a == b and hash_a == hash_b) or identity_check
        return value_equal
    except TypeError:
        if type(a) in [int, float]:
            return a == b
        elif isinstance(a, str):
            return a == b
        else:
            try:
                import json
                return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)
            except (TypeError, ValueError):
                return False
if __name__ == '__main__':
    x = 5
    y = 5
    z = [1, 2]
    w = [3, 4]
    s = "hello"
    t = "world"
    u = {"a": 1}
    v = {"b": 2}
    p = None
    q = None
    r = True
    n = False
    print(check_equality(x, y))             
    print(check_equality(z, w))                               
    print(check_equality(s, t))                              
    print(check_equality(u, v))                           
    print(check_equality(p, q))                       
    print(check_equality(r, n))