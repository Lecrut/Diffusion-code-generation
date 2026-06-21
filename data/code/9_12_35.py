class VolumeConverter:
    conversion_factors = {
        'cubic_meters_to_liters': 1000
    }

    @staticmethod
    def convert(volume, unit):
        if unit not in VolumeConverter.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        return volume * VolumeConverter.conversion_factors[unit]

if __name__ == '__main__':
    sample_volume_cubic_meters = 3.0
    converted_volume_liters = VolumeConverter.convert(sample_volume_cubic_meters, 'cubic_meters_to_liters')
    print(converted_volume_liters)