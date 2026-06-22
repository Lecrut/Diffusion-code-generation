class UnitConverter:
    @staticmethod
    def kilometers_to_meters(kilometers: float) -> float:
        if not isinstance(kilometers, (int, float)):
            raise TypeError("Input must be a number")
        if kilometers < 0:
            raise ValueError("Distance cannot be negative")
        return kilometers * 1000

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.kilometers_to_meters(5.5)
    print(result)