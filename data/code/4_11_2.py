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
    miles_value = 10.0
    km_result = converter.convert(miles_value, 'kilometers')
    print(f"{miles_value} miles is {km_result:.4f} kilometers")
    km_value = 16.0934496
    miles_result = converter.convert(km_value, 'miles')
    print(f"{km_value} kilometers is {miles_result:.4f} miles")
    zero_miles = 0
    zero_km = converter.convert(zero_miles, 'kilometers')
    print(f"{zero_miles} miles is {zero_km:.4f} kilometers")
    try:
        converter.convert("abc", 'miles')
    except TypeError as e:
        print(f"Caught expected error for non-numeric input: {e}")
    try:
        converter.convert(5, 'lightyears')
    except ValueError as e:
        print(f"Caught expected error for invalid unit: {e}")
    try:
        converter.convert(-5, 'miles')
    except ValueError as e:
        print(f"Caught expected error for negative distance: {e}")