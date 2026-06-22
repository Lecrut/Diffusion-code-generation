def is_valid_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    sides = [3, 4, 5]
    result = is_valid_triangle(sides[0], sides[1], sides[2])
    print(result)
    
    sides_invalid = [1, 2, 3]
    result_invalid = is_valid_triangle(sides_invalid[0], sides_invalid[1], sides_invalid[2])
    print(result_invalid)