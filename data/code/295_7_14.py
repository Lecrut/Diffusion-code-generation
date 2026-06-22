class SpeedConverter:
    def __init__(self):
        self.conversion_factor = 1.60934

    def convert_to_kmh(self, mph):
        return mph * self.conversion_factor

if __name__ == '__main__':
    converter = SpeedConverter()
    sample_speed_mph = 60
    converted_speed_kmh = converter.convert_to_kmh(sample_speed_mph)
    print(f"{sample_speed_mph} mph is equal to {converted_speed_kmh:.2f} km/h")