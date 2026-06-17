class VolumeConverter:
    def __init__(self):
        self.liters = 1.0
    def convert_to_liters(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        return value * self.liters
    def liters_to_gallons(self, liters: float) -> float:
        try:
            gallons = liters / 3.78541
            if not isinstance(gallons, (int, float)):
                raise TypeError("Conversion result must be numeric.")
            return gallons
        except Exception as e:
            raise RuntimeError(f"Error during conversion to gallons: {str(e)}")
    def liters_to_quarts(self, liters: float) -> float:
        try:
            quarts = liters * 1.05669
            if not isinstance(quarts, (int, float)):
                raise TypeError("Conversion result must be numeric.")
            return quarts
        except Exception as e:
            raise RuntimeError(f"Error during conversion to quarts: {str(e)}")
    def liters_to_pints(self, liters: float) -> float:
        try:
            pints = liters * 2.11338
            if not isinstance(pints, (int, float)):
                raise TypeError("Conversion result must be numeric.")
            return pints
        except Exception as e:
            raise RuntimeError(f"Error during conversion to pints: {str(e)}")
    def liters_to_milliliters(self, liters: float) -> float:
        try:
            milliliters = liters * 1000.0
            if not isinstance(milliliters, (int, float)):
                raise TypeError("Conversion result must be numeric.")
            return milliliters
        except Exception as e:
            raise RuntimeError(f"Error during conversion to milliliters: {str(e)}")
    def gallons_to_liters(self, gallons: float) -> float:
        try:
            liters = gallons * 3.78541
            if not isinstance(liters, (int, float)):
                raise TypeError("Conversion result must be numeric.")
            return liters
        except Exception as e:
            raise RuntimeError(f"Error during conversion to liters from gallons: {str(e)}")
    def quarts_to_liters(self, quarts: float) -> float:
        try:
            liters = quarts / 1.05669
            if not isinstance(liters, (int, float)):
                raise TypeError("Conversion result must be numeric.")
            return liters
        except Exception as e:
            raise RuntimeError(f"Error during conversion to liters from quarts: {str(e)}")
    def pints_to_liters(self, pints: float) -> float:
        try:
            liters = pints / 2.11338
            if not isinstance(liters, (int, float)):
                raise TypeError("Conversion result must be numeric.")
            return liters
        except Exception as e:
            raise RuntimeError(f"Error during conversion to liters from pints: {str(e)}")
    def milliliters_to_liters(self, milliliters: float) -> float:
        try:
            liters = milliliters / 1000.0
            if not isinstance(liters, (int, float)):
                raise TypeError("Conversion result must be numeric.")
            return liters
        except Exception as e:
            raise RuntimeError(f"Error during conversion to liters from milliliters: {str(e)}")
if __name__ == '__main__':
    converter = VolumeConverter()
    sample_values = [5.0, 10.0]
    for val in sample_values:
        try:
            print(f"Converting {val} liters to gallons:", end=" ")
            result_gallons = converter.liters_to_gallons(val)
            print(result_gallons)
            print(f"Converting {val} liters to quarts:", end=" ")
            result_quarts = converter.liters_to_quarts(val)
            print(result_quarts)
            print(f"Converting {val} liters to pints:", end=" ")
            result_pints = converter.liters_to_pints(val)
            print(result_pints)
            print(f"Converting {val} liters to milliliters:", end=" ")
            result_ml = converter.liters_to_milliliters(val)
            print(result_ml)
        except Exception as e:
            print(f"Error processing value {val}:", str(e))