class SpeedConverter:
    CONVERSION_FACTOR = 1.60934

    @staticmethod
    def mph_to_kmh(mph):
        return mph * SpeedConverter.CONVERSION_FACTOR

if __name__ == '__main__':
    sample_mph = 50
    kmh = SpeedConverter.mph_to_kmh(sample_mph)
    print(f"{sample_mph} mph is {kmh:.2f} km/h")