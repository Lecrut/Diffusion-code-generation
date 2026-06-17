from typing import Union
class VolumeConverter:
    def __init__(self):
        self.liters = 0
    def convert_to_liters(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            self.liters = abs(value)
        except Exception as e:
            raise ValueError(f"Invalid conversion error occurred: {e}")
    def convert_from_liters(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            self.liters = abs(value)
        except Exception as e:
            raise ValueError(f"Invalid conversion error occurred: {e}")
    def convert_to_gallons(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            self.liters = abs(value) * 0.264172
        except Exception as e:
            raise ValueError(f"Invalid conversion error occurred: {e}")
    def convert_from_gallons(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            self.liters = abs(value) / 0.264172
        except Exception as e:
            raise ValueError(f"Invalid conversion error occurred: {e}")
    def convert_to_quarts(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            self.liters = abs(value) * 1.05669
        except Exception as e:
            raise ValueError(f"Invalid conversion error occurred: {e}")
    def convert_from_quarts(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            self.liters = abs(value) / 1.05669
        except Exception as e:
            raise ValueError(f"Invalid conversion error occurred: {e}")
    def convert_to_pints(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            self.liters = abs(value) * 2.11338
        except Exception as e:
            raise ValueError(f"Invalid conversion error occurred: {e}")
    def convert_from_pints(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            self.liters = abs(value) / 2.11338
        except Exception as e:
            raise ValueError(f"Invalid conversion error occurred: {e}")
    def convert_to_milliliters(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            self.liters = abs(value) * 1000
        except Exception as e:
            raise ValueError(f"Invalid conversion error occurred: {e}")
    def convert_from_milliliters(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            self.liters = abs(value) / 1000
        except Exception as e:
            raise ValueError(f"Invalid conversion error occurred: {e}")
if __name__ == '__main__':
    converter = VolumeConverter()
    try:
        converter.convert_to_liters(5)
        print("Converted 5 units (assumed base input for demo logic)")
        gallons = 10.0
        converter.convert_from_gallons(gallons)
        print(f"Converted {gallons} gallons to liters: {converter.liters}")
        quarts = 25.0
        converter.convert_from_quarts(quarts)
        print(f"Converted {quarts} quarts to liters: {converter.liters}")
        pints = 100.0
        converter.convert_from_pints(pints)
        print(f"Converted {pints} pints to liters: {converter.liters}")
        milliliters = 5000.0
        converter.convert_from_milliliters(milliliters)
        print(f"Converted {milliliters} milliliters to liters: {converter.liters}")
    except Exception as e:
        print(f"Error during conversion: {e}")