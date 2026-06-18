def check_match(value1: any, value2: any) -> bool:
    return value1 is value2 and value1 == value2
if __name__ == '__main__':
    a = 5
    b = "hello"
    c = [1, 2, 3]
    d = (4, 5, 6)
    print(check_match(a, a))            
    print(check_match(b, b))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    print(check_match(c, c))                                 
    print(check_match(d, d))            
    x = 5
    y = 5
    z = "hi"
    print(f"x is y: {x is y}, x == y: {x == y}") 
    print(check_match(x, y))