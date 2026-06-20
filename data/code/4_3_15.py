class UnitConverter:
    METERS_TO_FEET = 3.280839895
    FEET_TO_METERS = 0.3048
    KILOGRAMS_TO_POUNDS = 2.20462262185
    POUNDS_TO_KILOGRAMS = 0.45359237
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
    CELSIUS_TO_FAHRENHEIT_OFFSET = 32
    FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
    FAHRENHEIT_TO_CELSIUS_OFFSET = 32
    LITERS_TO_GALLONS = 0.264172052
    GALLONS_TO_LITERS = 3.785411784

    @staticmethod
    def _check_numeric(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number")

    @staticmethod
    def _check_non_negative(value):
        if value < 0:
            raise ValueError("Input cannot be negative for this conversion")

    def convert_meters_to_feet(self, meters):
        self._check_numeric(meters)
        self._check_non_negative(meters)
        return meters * self.METERS_TO_FEET

    def convert_feet_to_meters(self, feet):
        self._check_numeric(feet)
        self._check_non_negative(feet)
        return feet * self.FEET_TO_METERS

    def convert_kilograms_to_pounds(self, kilograms):
        self._check_numeric(kilograms)
        self._check_non_negative(kilograms)
        return kilograms * self.KILOGRAMS_TO_POUNDS

    def convert_pounds_to_kilograms(self, pounds):
        self._check_numeric(pounds)
        self._check_non_negative(pounds)
        return pounds * self.POUNDS_TO_KILOGRAMS

    def convert_celsius_to_fahrenheit(self, celsius):
        self._check_numeric(celsius)
        return (celsius * self.CELSIUS_TO_FAHRENHEIT_FACTOR) + self.CELSIUS_TO_FAHRENHEIT_OFFSET

    def convert_fahrenheit_to_celsius(self, fahrenheit):
        self._check_numeric(fahrenheit)
        return (fahrenheit - self.FAHRENHEIT_TO_CELSIUS_OFFSET) * self.FAHRENHEIT_TO_CELSIUS_FACTOR

    def convert_liters_to_gallons(self, liters):
        self._check_numeric(liters)
        self._check_non_negative(liters)
        return liters * self.LITERS_TO_GALLONS

    def convert_gallons_to_liters(self, gallons):
        self._check_numeric(gallons)
        self._check_non_negative(gallons)
        return gallons * self.GALLONS_TO_LITERS

if __name__ == '__main__':
    converter = UnitConverter()
    print(converter.convert_meters_to_feet(100))
    print(converter.convert_kilograms_to_pounds(50))
    print(converter.convert_celsius_to_fahrenheit(37))
    print(converter.convert_fahrenheit_to_celsius(98.6))
    print(converter.convert_liters_to_gallons(10))