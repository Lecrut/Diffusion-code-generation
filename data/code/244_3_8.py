def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    trapezoid_base1 = 5
    trapezoid_base2 = 7
    trapezoid_height = 4
    parallelogram_base = 6
    parallelogram_height = 3
    
    trapezoid_result = trapezoid_area(trapezoid_base1, trapezoid_base2, trapezoid_height)
    parallelogram_result = parallelogram_area(parallelogram_base, parallelogram_height)
    
    total_area = trapezoid_result + parallelogram_result
    print(total_area)