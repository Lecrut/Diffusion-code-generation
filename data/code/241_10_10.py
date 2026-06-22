def calculate_area(width: float, height: float) -> float:
    return width * height

if __name__ == '__main__':
    sample_values = {
        'width': 5.0,
        'height': 3.0
    }
    result = calculate_area(sample_values['width'], sample_values['height'])
    print(result)