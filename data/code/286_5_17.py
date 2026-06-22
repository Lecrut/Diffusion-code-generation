class UnitConverter:
    NANOMETERS_TO_METERS = 1e-9

    @staticmethod
    def nanometers_to_meters(nanometers):
        return nanometers * UnitConverter.NANOMETERS_TO_METERS

if __name__ == '__main__':
    sample_nanometers = 500_000_000
    meters = UnitConverter.nanometers_to_meters(sample_nanometers)
    print(f"{sample_nanometers} nanometers is equal to {meters:.9f} meters")