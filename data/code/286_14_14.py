class Conversion:
    YARDS_TO_METERS = 0.9144

    @staticmethod
    def yards_to_meters(yards):
        return [y * Conversion.YARDS_TO_METERS for y in yards]

if __name__ == '__main__':
    measurements = [1.0, 5.0, 10.5, 100.0]
    meters_measurements = Conversion.yards_to_meters(measurements)
    print(meters_measurements)