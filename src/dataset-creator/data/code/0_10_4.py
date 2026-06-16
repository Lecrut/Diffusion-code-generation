def values_match(*args):
    if len(args) != 2:
        return False
    a, b = args
    try:
        type_a = type(a)
        type_b = type(b)
        if isinstance(type_a, type) and not hasattr(type_a, '__dict__'):
            return a is b
        return a == b
    except TypeError:
        return False
if __name__ == '__main__':
    print(values_match(5, 5))                    
    print(values_match("hello", "world"))                  
    print(values_match((1,2), (1,2)))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    def values_match_v2(*args):
        if len(args) != 2: return False
        a, b = args
        try:
            if isinstance(a, (int, float)) or isinstance(b, (int, float)):
                return a is b
            elif isinstance(a, str) and isinstance(b, str):
                return a is b
            elif isinstance(a, tuple) and isinstance(b, tuple):
                return a == b
            else:
                return a == b
        except TypeError:
            return False
    print(values_match_v2(10, 10))                       
    print(values_match_v2("test", "test"))                                                                                                                                                                                                                                                                                  
    pass
if __name__ == '__main__':
    print(values_match(5, 5))                       
    print(values_match("a", "b"))                                                          
    print(values_match((1,), (1,)))                                                                                                                                                    
    print(values_match(10, 20))                                                                                                               
    print(values_match("x", "y"))            
def final_values_match(*args):
    if len(args) != 2: return False
    a, b = args
    try:
        is_immutable_primitive = isinstance(a, int) or isinstance(b, int) or\
                                isinstance(a, float) or isinstance(b, float)
        if is_immutable_primitive:
            return a is b
        return a == b
    except TypeError:
        return False
if __name__ == '__main__':
    print(final_values_match(5, 5))                       
    print(final_values_match("a", "b"))                                                  
    print(final_values_match((1,), (1,)))                                                                                                                                                                               
    print(final_values_match(5, 5))            
    print(final_values_match("a", "b"))