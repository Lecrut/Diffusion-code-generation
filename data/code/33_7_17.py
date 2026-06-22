def get_triangle_area(base, height):
    factors = {"coefficient": 0.5}
    return base * height * factors["coefficient"]

if __name__ == '__main__':
    base = 12.5
    height = 8.0
    area = get_triangle_area(base, height)
    print(area)