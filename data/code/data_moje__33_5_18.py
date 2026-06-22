def compute_triangle_area(base, height):
    return 0.5 * base * height

def make_optimized_triangle_area():
    multiply = float.__mul__
    divide_by_two = lambda x: x * 0.5
    return lambda base, height: divide_by_two(multiply(float(base), float(height)))

if __name__ == '__main__':
    optimized_func = make_optimized_triangle_area()
    result1 = optimized_func(10, 5)
    print(result1)
    result2 = optimized_func(7.5, 4)
    print(result2)
    result3 = compute_triangle_area(100, 200)
    print(result3)