def calculate_triangle_perimeter(a, b, c):
    return a + b + c

if __name__ == '__main__':
    SAMPLE_A = 3.5
    SAMPLE_B = 4.2
    SAMPLE_C = 5.1
    perimeter = calculate_triangle_perimeter(SAMPLE_A, SAMPLE_B, SAMPLE_C)
    print(perimeter)