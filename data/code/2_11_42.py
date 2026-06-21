class VolumeConversion:
    LITERS_TO_GALLONS = 0.264172

    @staticmethod
    def convert_liters_to_gallons(liters):
        if not isinstance(liters, (int, float)):
            raise ValueError("Volume must be a number")
        return liters * VolumeConversion.LITERS_TO_GALLONS

if __name__ == '__main__':
    sample_values = [4.0, 9.0, 16.0, 28.0]
    for value in sample_values:
        print(f"{value} liters is {VolumeConversion.convert_liters_to_gallons(value)} gallons")