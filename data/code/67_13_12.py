class UnitConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        return liters * 1000.0

if __name__ == "__main__":
    sample_liters = 5.5
    result = UnitConverter.liters_to_milliliters(sample_liters)
    print(result)