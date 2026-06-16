class WeightSystem:
    def __init__(self):
        self.conversion_factors = {"kg_to_lb": 2.20462, "lb_to_kg": 0.453592}
    def add_conversion_factor(self, factor_name, factor_value):
        self.conversion_factors[factor_name] = factor_value
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("One or both units are not supported.")
        if from_unit == "kg" and to_unit == "lb":
            if "kg_to_lb" in self.conversion_factors:
                return value * self.conversion_factors["kg_to_lb"]
        elif from_unit == "lb" and to_unit == "kg":
            if "lb_to_kg" in self.conversion_factors:
                return value * self.conversion_factors["lb_to_kg"]
        else:
            raise NotImplementedError(f"Conversion from {from_unit} to {to_unit} is not implemented.")
if __name__ == '__main__':
    ws = WeightSystem()
    print("Initial conversion factors:", ws.conversion_factors)
    ws.add_conversion_factor("m_to_ft", 3.28084)
    print("\nAfter adding m_to_ft:", ws.conversion_factors)
    try:
        result1 = ws.convert(10, "kg", "lb")
        print("\n10 kg to lb:", result1)
        result2 = ws.convert(10, "m", "ft")
        print("10 m to ft:", result2)
        result3 = ws.convert(5, "lb", "kg")
        print("5 lb to kg:", result3)
        result4 = ws.convert(10, "kg", "kg")
        print("10 kg to kg:", result4)
    except (ValueError, NotImplementedError) as e:
        print(f"\nError during conversion: {e}")