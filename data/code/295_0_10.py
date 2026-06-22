class DistanceConverter:
    METERS_TO_KILOMETERS = 0.001

    @staticmethod
    def meters_to_kilometers(meters):
        return round(meters * DistanceConverter.METERS_TO_KILOMETERS, 2)

if __name__ == '__main__':
    meters_value = 1500.0
    kilometers_value = DistanceConverter.meters_to_kilometers(meters_value)
    print(f"{meters_value} meters is equal to {kilometers_value} kilometers")