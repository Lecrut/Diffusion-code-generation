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
    def milliliters_to_liters(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return self.convert_to_liters(float(value)) / 1000.0
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
    def milliliters_to_gallons(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return self.convert_to_liters(float(value)) / 3785.411784
        except OverflowError:
            raise ValueError("Number is too large to convert.")
    def milliliters_to_quarts(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return self.convert_to_liters(float(value)) / 0.946352946 * 1000.0
        except OverflowError:
            raise ValueError("Number is too large to convert.")
    def milliliters_to_pints(self, value: float) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be a number.")
        try:
            return self.convert_to_liters(float(value)) / 0.4731764759 * 1000.0
        except OverflowError:
            raise ValueError("Number is too large to convert.")
if __name__ == '__main__':
    converter = VolumeConverter()
    sample_values = {
        "liters": [2.5, -1.0],
        "gallons": [3.785411784, 0.5],
        "quarts": [9.46352946, 1.0],
        "pints": [18.93705892, 2.0],
        "milliliters": [2500.0, -500.0]
    }
    for unit in sample_values:
        try:
            result = converter.convert_to_liters(sample_values[unit][0]) if unit != 'liters' else sample_values[unit][0]
            print(f"{unit.capitalize()} to Liters ({sample_values[unit][0]}): {result}")
            reverse_result = None
            for u, v in sample_values.items():
                if u == unit:
                    continue
                try:
                    rev_val = converter.convert_to_liters(v[1]) / 3.785411784 * (v[0] / v[1])                            
                    break 
                except ValueError:
                    pass
            print(f"Liters to {unit.capitalize()} ({result}): {reverse_result}")
        except Exception as e:
            print(f"Error processing {sample_values[unit]}: {e}")
    invalid_inputs = ["abc", None, 123.456]
    for inp in invalid_inputs:
        try:
            converter.convert_to_liters(inp)
        except (TypeError, ValueError):
            print(f"Correctly handled invalid input type or value: {inp}")