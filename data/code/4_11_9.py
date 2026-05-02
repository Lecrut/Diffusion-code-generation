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
if __name__ == '__main__':
    converter = DistanceConverter()
    miles_value = 10.0
    try:
        km_result = converter.convert(miles_value, 'kilometers')
        print(f"{miles_value} miles is equal to {km_result:.4f} kilometers")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    km_value = 16.0934496
    try:
        miles_result = converter.convert(km_value, 'miles')
        print(f"{km_value} kilometers is equal to {miles_result:.4f} miles")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    zero_miles = 0
    try:
        km_zero = converter.convert(zero_miles, 'kilometers')
        print(f"{zero_miles} miles is equal to {km_zero:.4f} kilometers")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    try:
        converter.convert(5, 'lightyears')
    except (TypeError, ValueError) as e:
        print(f"Caught expected error for invalid unit: {e}")
    try:
        converter.convert("ten", 'miles')
    except (TypeError, ValueError) as e:
        print(f"Caught expected error for invalid type: {e}")
    try:
        converter.convert(-5, 'miles')
    except (TypeError, ValueError) as e:
        print(f"Caught expected error for negative distance: {e}")