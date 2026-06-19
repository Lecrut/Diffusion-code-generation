def can_form_triangle(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    sample_values = [3, 4, 5]
    print(can_form_triangle(sample_values))