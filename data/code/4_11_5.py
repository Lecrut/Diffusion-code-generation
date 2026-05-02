class DistanceConverter:
    def convert(self, distance, unit):
        if not isinstance(distance, (int, float)):
            raise TypeError("Distance must be a numeric value.")
        if unit not in ['miles', 'kilometers']:
            raise ValueError("Unit must be either 'miles' or 'kilometers'.")
        if unit == 'miles':
            if distance < 0:
                raise ValueError("Distance cannot be negative.")
            return distance
        elif unit == 'kilometers':
            if distance < 0:
                raise ValueError("Distance cannot be negative.")
            return distance * 1.60934496
        return None
if __name__ == '__main__':
    converter = DistanceConverter()
    miles_value = 10
    km_result = converter.convert(miles_value, 'miles')
    print(f"{miles_value} miles is {km_result} kilometers")
    km_value = 5
    km_result_2 = converter.convert(km_value, 'kilometers')
    print(f"{km_value} kilometers is {km_result_2} kilometers")
    miles_value_2 = 100
    km_result_3 = converter.convert(miles_value_2, 'kilometers')
    print(f"{miles_value_2} miles is {km_result_3} kilometers")
    try:
        converter.convert("abc", 'miles')
    except TypeError as e:
        print(f"Caught expected error for non-numeric input: {e}")
    try:
        converter.convert(10, 'furlongs')
    except ValueError as e:
        print(f"Caught expected error for invalid unit: {e}")
    try:
        converter.convert(-5, 'miles')
    except ValueError as e:
        print(f"Caught expected error for negative distance: {e}")