from functools import reduce

calculate_triangle_area = lambda base, height: (base * height) / 2

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    result = calculate_triangle_area(sample_base, sample_height)
    print(result)