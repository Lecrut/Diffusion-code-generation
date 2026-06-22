import math

class UnitConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        if not isinstance(liters, (int, float)):
            raise TypeError("Input must be a number")
        if liters < 0:
            raise ValueError("Volume cannot be negative")
        return math.floor(liters * 1000 + 0.5)

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.liters_to_milliliters(2.5)
    print(result)
    result2 = converter.liters_to_milliliters(0.001)
    print(result2)