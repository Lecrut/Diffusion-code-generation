class DistanceConverter:
    def __init__(self):
        self.miles_to_kilometers = 1.60934
        self.kilometers_to_miles = 0.621371

    def convert(self, value, unit_from, unit_to):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be a numeric type")
        
        if unit_from == 'miles' and unit_to == 'kilometers':
            return value * self.miles_to_kilometers
        elif unit_from == 'kilometers' and unit_to == 'miles':
            return value * self.kilometers_to_miles
        else:
            raise ValueError("Invalid units. Use 'miles' or 'kilometers'.")

if __name__ == '__main__':
    converter = DistanceConverter()
    miles_value = 10
    kilometers_value = 16.0934

    print(f"{miles_value} miles is {converter.convert(miles_value, 'miles', 'kilometers')} kilometers")
    print(f"{kilometers_value} kilometers is {converter.convert(kilometers_value, 'kilometers', 'miles')} miles")