class VolumeConversion:
    conversion_table = {
        'cubic_meters_to_liters': 1000,
        'liters_to_cubic_meters': 0.001
    }

    @staticmethod
    def convert(volume, from_unit, to_unit):
        if from_unit not in VolumeConversion.conversion_table or to_unit not in VolumeConversion.conversion_table:
            raise ValueError("Unsupported unit conversion")
        
        conversion_key = f"{from_unit}_to_{to_unit}"
        if conversion_key not in VolumeConversion.conversion_table:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported")
        
        return volume * VolumeConversion.conversion_table[conversion_key]

if __name__ == '__main__':
    sample_volume_cubic_meters = 5.0
    converted_volume_liters = VolumeConversion.convert(sample_volume_cubic_meters, 'cubic_meters', 'liters')
    print(converted_volume_liters)