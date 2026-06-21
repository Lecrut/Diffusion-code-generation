class VolumeConverter:
    LITERS_PER_GALLON = 3.78541

    def __init__(self):
        self.conversion_factor = self.LITERS_PER_GALLON

    def convert_gallons_to_liters(self, gallons):
        if gallons < 0:
            raise ValueError("Gallons cannot be negative")
        return gallons * self.conversion_factor

if __name__ == '__main__':
    sample_volume_gallons1 = 3.0
    sample_volume_gallons2 = 8.5
    converter = VolumeConverter()
    
    converted_liters1 = converter.convert_gallons_to_liters(sample_volume_gallons1)
    print(converted_liters1)
    
    converted_liters2 = converter.convert_gallons_to_liters(sample_volume_gallons2)
    print(converted_liters2)