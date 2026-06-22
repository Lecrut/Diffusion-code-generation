def can_form_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c

if __name__ == '__main__':
    sample_values = [3, 4, 5]
    print(can_form_triangle(sample_values))