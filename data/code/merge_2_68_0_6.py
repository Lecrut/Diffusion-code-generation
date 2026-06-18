class VolumeConverter:
    def __init__(self):
        self.liters = 1.0
    def convert_to_liters(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return float(value) * self.liters
        except OverflowError:
            raise ValueError("Number is too large to convert.")
    def liters_to_gallons(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return self.convert_to_liters(float(value)) / 3.785411784
        except OverflowError:
            raise ValueError("Number is too large to convert.")
    def liters_to_quarts(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return self.convert_to_liters(float(value)) / 0.946352946
        except OverflowError:
            raise ValueError("Number is too large to convert.")
    def liters_to_pints(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return self.convert_to_liters(float(value)) / 0.4731764759
        except OverflowError:
            raise ValueError("Number is too large to convert.")
    def liters_to_milliliters(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return self.convert_to_liters(float(value)) * 1000.0
        except OverflowError:
            raise ValueError("Number is too large to convert.")
    def gallons_to_liters(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return self.convert_to_liters(float(value)) * 3.785411784
        except OverflowError:
            raise ValueError("Number is too large to convert.")
    def quarts_to_liters(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return self.convert_to_liters(float(value)) * 0.946352946
        except OverflowError:
            raise ValueError("Number is too large to convert.")
    def pints_to_liters(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return self.convert_to_liters(float(value)) * 0.4731764759
        except OverflowError:
            raise ValueError("Number is too large to convert.")
    def milliliters_to_liters(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return self.convert_to_liters(float(value)) / 1000.0
        except OverflowError:
            raise ValueError("Number is too large to convert.")
if __name__ == '__main__':
    converter = VolumeConverter()
    sample_values = {
        "liters": [5, -2],
        "gallons": [10.5, 0],
        "quarts": [8, 3.75],
        "pints": [4, 6],
        "milliliters": [1000, 50]
    }
    for unit in sample_values:
        try:
            result = converter.convert_to_liters(sample_values[unit][0]) if unit != 'liters' else sample_values[unit][0]
            print(f"{unit.capitalize()} to Liters (Sample {sample_values[unit][0]}): {result}")
            for val in sample_values[unit]:
                try:
                    converted = converter.convert_to_liters(val)
                    if unit != 'liters':
                        original_name = f"1 {unit}"
                        print(f"{original_name} to Liters (Sample {val}): {converted}")
                except ValueError as e:
                    print(f"Error converting {sample_values[unit][0]} of {unit}: {e}")
        except Exception as e:
            print(f"Unexpected error processing unit '{unit}': {e}")
    try:
        converter.convert_to_liters("invalid")
    except TypeError as e:
        print(f"Caught expected type error for string input: {e}")