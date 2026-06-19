def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    sample_values = {
        "base": 12.3,
        "height": 7.8
    }
    area = calculate_triangle_area(sample_values["base"], sample_values["height"])
    print(area)