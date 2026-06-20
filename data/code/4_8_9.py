import sys

class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 0.621371

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.lower()

    def convert_to_kilometers(self):
        if self.unit == 'miles':
            return self.value * self.MILES_TO_KILOMETERS
        elif self.unit == 'kilometers':
            return self.value
        else:
            raise ValueError("Unit must be 'miles' or 'kilometers'")

    def convert_to_miles(self):
        if self.unit == 'kilometers':
            return self.value * self.KILOMETERS_TO_MILES
        elif self.unit == 'miles':
            return self.value
        else:
            raise ValueError("Unit must be 'miles' or 'kilometers'")

    def display_conversion(self):
        km_value = self.convert_to_kilometers()
        miles_value = self.convert_to_miles()
        return f"{self.value} {self.unit} is {km_value:.4f} kilometers and {miles_value:.4f} miles"

def run_conversion(value, unit):
    converter = DistanceConverter(value, unit)
    return converter.display_conversion()

if __name__ == '__main__':
    sample_value = 100
    sample_unit = 'kilometers'
    result = run_conversion(sample_value, sample_unit)
    print(result)

    sample_value_2 = 50
    sample_unit_2 = 'miles'
    result_2 = run_conversion(sample_value_2, sample_unit_2)
    print(result_2)