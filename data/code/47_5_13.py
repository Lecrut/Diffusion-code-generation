def calculate_triangle_area(base, height):
    return 0.5 * base * height

def read_inputs_from_file(file_content):
    lines = file_content.strip().split('\n')
    inputs = []
    for line in lines:
        base, height = map(float, line.split())
        inputs.append((base, height))
    return inputs

def process_triangle_areas(inputs):
    areas = []
    for base, height in inputs:
        area = calculate_triangle_area(base, height)
        areas.append(area)
    return areas

if __name__ == '__main__':
    sample_file_content = """3 4
5 6
7 8"""
    triangle_inputs = read_inputs_from_file(sample_file_content)
    triangle_areas = process_triangle_areas(triangle_inputs)
    print(triangle_areas)