class DistanceConverter:

    def __init__(self):
        self.miles_to_kilometers = 1.60934
        self.kilometers_to_miles = 0.621371

    def convert(self, distance, unit):
        if not isinstance(distance, (int, float)):
            raise ValueError('Distance must be a numeric value.')
        if unit.lower() == 'miles':
            return distance * self.miles_to_kilometers
        elif unit.lower() == 'kilometers':
            return distance * self.kilometers_to_miles
        else:
            raise ValueError("Unit must be either 'miles' or 'kilometers'.")
if __name__ == '__main__':
    converter = DistanceConverter()
    miles_distance = 10
    kilometers_distance = 16.0934
    print(f"{miles_distance} miles is {converter.convert(miles_distance, 'miles')} kilometers")
    print(f"{kilometers_distance} kilometers is {converter.convert(kilometers_distance, 'kilometers')} miles")