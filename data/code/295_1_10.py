class TemperatureConverter:
    def __init__(self):
        self.conversion_factor = 0.264172

    def liters_to_gallons(self, liters):
        return liters * self.conversion_factor

if __name__ == '__main__':
    converter = TemperatureConverter()
    sample_liters = 5
    gallons = converter.liters_to_gallons(sample_liters)
    print(f"{sample_liters} liters is {gallons:.2f} gallons")