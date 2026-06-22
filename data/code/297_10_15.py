class DistanceConverter:

    def __init__(self):
        self.meter_to_km = 0.001

    def convert(self, meters):
        if meters < 0:
            raise ValueError('Negative input not allowed')
        return meters * self.meter_to_km
if __name__ == '__main__':
    converter = DistanceConverter()
    print(converter.convert(1000))
    try:
        print(converter.convert(-500))
    except ValueError as e:
        print(e)