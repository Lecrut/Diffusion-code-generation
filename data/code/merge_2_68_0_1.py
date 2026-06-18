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
    sample_inputs = [5, 2]
    for input_val in sample_inputs:
        try:
            gallons = converter.liters_to_gallons(input_val)
            quarts = converter.liters_to_quarts(input_val)
            pints = converter.liters_to_pints(input_val)
            ml = converter.liters_to_milliliters(input_val)
            print(f"Input: {input_val} Liters")
            print(f"Gallons: {gallons}")
            print(f"Quarts: {quarts}")
            print(f"Pints: {pints}")
            print(f"Milliliters: {ml}\n")
        except (TypeError, ValueError) as e:
            print(f"Error converting {input_val}: {e}\n")
    try:
        converter.liters_to_gallons("invalid")
    except Exception as error:
        print(f"Catch invalid input type: {error}")