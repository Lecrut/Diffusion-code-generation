def is_identical(value1: object, value2: object) -> bool:
    return isinstance(value1, object) and isinstance(value2, object) and value1 is value2
if __name__ == '__main__':
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = "hello"
    d = "hello"
    e = (5,)
    f = (5,)
    g = None
    print(f"is_identical(a, b) -> {is_identical(a, b)}")                                 
    print(f"is_identical(c, d) -> {is_identical(c, d)}")                                                                                                         
    h = "world"
    i = "hello" + " world".replace(" ", "")                                                            
    print(f"is_identical(c, d) -> {is_identical(c, d)}")                                                                                                                                                                                                                                     
    print(f"is_identical(a, b) -> {is_identical(a, b)}")         
    j = a.append(4); k = [1,2,3]; l = [1,2,3]
    m = None; n = None
    print(f"is_identical(m, n) -> {is_identical(m, n)}")