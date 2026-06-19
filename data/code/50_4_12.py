class AreaCalculator:
    @staticmethod
    def convert_to_float(area_str):
        try:
            return float(area_str)
        except ValueError as e:
            print(f"ValueError: {e}")
            return None

    @staticmethod
    def calculate_difference(area1_str, area2_str):
        area1 = AreaCalculator.convert_to_float(area1_str)
        area2 = AreaCalculator.convert_to_float(area2_str)
        
        if area1 is not None and area2 is not None:
            return abs(area1 - area2)
        else:
            return None

if __name__ == '__main__':
    sample_area1 = "75.2"
    sample_area2 = "30.8"
    difference = AreaCalculator.calculate_difference(sample_area1, sample_area2)
    if difference is not None:
        print(difference)