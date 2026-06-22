def calculate_triangle_areas(file_content):
    areas = []
    lines = file_content.strip().split('\n')
    for line in lines:
        base, height = map(float, line.split())
        area = 0.5 * base * height
        areas.append(area)
    return areas

if __name__ == '__main__':
    sample_input = """3 4
5 12
8 6"""
    result = calculate_triangle_areas(sample_input)
    print(result)