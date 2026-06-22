class DistanceConverter:
    def __init__(self, distance, unit):
        self.distance = distance
        self.unit = unit

    def convert(self):
        if self.unit.lower() == 'kilometers':
            return self.distance * 0.621371
        elif self.unit.lower() == 'miles':
            return self.distance / 0.621371
        else:
            raise ValueError("Invalid unit. Please use 'kilometers' or 'miles'.")

if __name__ == '__main__':
    converter = DistanceConverter(10, 'kilometers')
    print(converter.convert())