class WeightSystem:
    def __init__(self):
        self.conversion_factors = {"kg_to_lb": 2.20462, "lb_to_kg": 0.453592}
    def add_conversion_factor(self, factor_name, factor_value):
        self.conversion_factors[factor_name] = factor_value
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit in self.conversion_factors and to_unit in self.conversion_factors:
            if from_unit == "kg" and to_unit == "lb":
                if "kg_to_lb" in self.conversion_factors:
                    return value * self.conversion_factors["kg_to_lb"]
            elif from_unit == "lb" and to_unit == "kg":
                if "lb_to_kg" in self.conversion_factors:
                    return value * self.conversion_factors["lb_to_kg"]
        raise ValueError(f"Conversion not supported or factors missing for {from_unit} to {to_unit}")
if __name__ == '__main__':
    ws = WeightSystem()
    print("Initial conversion factors:", ws.conversion_factors)
    ws.add_conversion_factor("lb_to_oz", 16)
    print("\nAfter adding lb_to_oz:", ws.conversion_factors)
    try:
        result1 = ws.convert(10, "kg", "lb")
        print("10 kg to lb:", result1)
        result2 = ws.convert(50, "lb", "oz")
        print("50 lb to oz:", result2)
        result3 = ws.convert(10, "kg", "kg")
        print("10 kg to kg:", result3)
        result4 = ws.convert(10, "lb", "kg")
        print("10 lb to kg:", result4)
    except ValueError as e:
        print("Error during conversion:", e)