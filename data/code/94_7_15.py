from typing import Iterable, Any

ANY_TRUE = True
NO_MATCH = False

def check_any_truthy(values: Iterable[Any]) -> bool:
    truthiness_map = {
        bool: lambda x: x,
        int: lambda x: x != 0,
        float: lambda x: x != 0.0,
        str: lambda x: len(x) > 0,
        type(None): lambda x: False,
    }
    
    for val in values:
        val_type = type(val)
        
        if val_type in truthiness_map:
            if truthiness_map[val_type](val):
                return ANY_TRUE
        else:
            if val:
                return ANY_TRUE
                
    return NO_MATCH

if __name__ == '__main__':
    sample_true = [0, "", False, None, 0.0, {"key": "val"}]
    sample_false = [0, "", False, None, 0.0, {}]
    sample_empty = []
    
    print(check_any_truthy(sample_true))
    print(check_any_truthy(sample_false))
    print(check_any_truthy(sample_empty))
    print(check_any_truthy([1, 2, 3]))
    print(check_any_truthy([None, False, ""]))