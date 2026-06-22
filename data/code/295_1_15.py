class Conversion:
    def __init__(self):
        self.conversion_factor = 0.264172

    def liters_to_gallons(self, liters):
        return liters * self.conversion_factor

if __name__ == '__main__':
    converter = Conversion()
    sample_liters = 10
    gallons = converter.liters_to_gallons(sample_liters)
    print(f"{sample_liters} liters is {gallons:.2f} gallons")