def _is_truthy(value):
    truthy_map = {
        int: lambda v: v != 0,
        float: lambda v: v != 0.0,
        str: lambda v: len(v) > 0,
        list: lambda v: len(v) > 0,
        tuple: lambda v: len(v) > 0,
        dict: lambda v: len(v) > 0,
        set: lambda v: len(v) > 0,
        bool: lambda v: v is True,
    }
    type_func = truthy_map.get(type(value))
    if type_func is not None:
        return type_func(value)
    if value is None:
        return False
    if isinstance(value, (bool,)):
        return value
    return bool(value)

def determine_both_false(val1, val2):
    is_val1_truthy = _is_truthy(val1)
    is_val2_truthy = _is_truthy(val2)
    return not is_val1_truthy and not is_val2_truthy

if __name__ == '__main__':
    val_a = 0
    val_b = 0
    print(determine_both_false(val_a, val_b))
    
    val_c = 1
    val_d = 0
    print(determine_both_false(val_c, val_d))
    
    val_e = None
    val_f = None
    print(determine_both_false(val_e, val_f))
    
    val_g = [1, 2]
    val_h = {}
    print(determine_both_false(val_g, val_h))
    
    val_i = "hello"
    val_j = ""
    print(determine_both_false(val_i, val_j))