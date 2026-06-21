def is_valid_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    result = is_valid_triangle(3, 4, 5)
    print(result)
    
    result2 = is_valid_triangle(1, 2, 3)
    print(result2)
    
    result3 = is_valid_triangle(7, 10, 5)
    print(result3)