class LengthConverter:

    def km_to_miles(self, kilometers: float) -> float:
        return kilometers * 0.621371
if __name__ == '__main__':
    converter = LengthConverter()
    print(converter.km_to_miles(1))
    print(converter.km_to_miles(5))
    print(converter.km_to_miles(10))
    print(converter.km_to_miles(100))