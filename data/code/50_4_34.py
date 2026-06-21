class AreaCalculator:
    def __init__(self):
        self.previous_area = None

    def area_difference_generator(self, *areas):
        for area in areas:
            if self.previous_area is not None:
                yield abs(area - self.previous_area)
            self.previous_area = area

if __name__ == '__main__':
    sample_areas = [12, 34, 56, 78, 90]
    calculator = AreaCalculator()
    differences = list(calculator.area_difference_generator(*sample_areas))
    print(differences)