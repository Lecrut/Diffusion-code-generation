def area_difference_generator(*areas):
    if not all(isinstance(area, (int, float)) and area >= 0 for area in areas):
        raise ValueError("All areas must be non-negative numbers.")
    
    previous_area = None
    for area in areas:
        if previous_area is not None:
            yield abs(area - previous_area)
        previous_area = area

class AreaCalculator:
    def __init__(self, *areas):
        self.areas = areas

    def calculate_differences(self):
        return list(area_difference_generator(*self.areas))

if __name__ == '__main__':
    sample_areas = [100, 200, 150, 300, 400]
    calculator = AreaCalculator(*sample_areas)
    
    try:
        differences = calculator.calculate_differences()
        print(differences)
    except ValueError as e:
        print(e)