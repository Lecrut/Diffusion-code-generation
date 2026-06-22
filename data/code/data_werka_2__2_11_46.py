class VolumeConverter:
    LITERS_TO_GALLONS_RATE = 0.264172

    @staticmethod
    def convert_liters_to_gallons(liters):
        if not isinstance(liters, (int, float)):
            raise ValueError("Volume must be a number")
        return liters * VolumeConverter.LITERS_TO_GALLONS_RATE

if __name__ == '__main__':
    sample_values = [5.0, 10.0, 15.0, 20.0]
    for value in sample_values:
        print(f"{value} liters is {VolumeConverter.convert_liters_to_gallons(value)} gallons")