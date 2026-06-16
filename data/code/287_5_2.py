class WeightSystem:
    def __init__(self):
        self.conversion_factors = {
            "kg_to_lb": 2.20462,
            "lb_to_kg": 0.453592,
            "g_to_kg": 0.001
        }
    def add_conversion_factor(self, factor_name, factor_value):
        self.conversion_factors[factor_name] = factor_value
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "kg" and to_unit == "lb":
            if "kg_to_lb" in self.conversion_factors:
                return value * self.conversion_factors["kg_to_lb"]
            elif "lb_to_kg" in self.conversion_factors:
                return value / self.conversion_factors["lb_to_kg"]
        elif from_unit == "lb" and to_unit == "kg":
            if "lb_to_kg" in self.conversion_factors:
                return value * self.conversion_factors["lb_to_kg"]
            elif "kg_to_lb" in self.conversion_factors:
                return value / self.conversion_factors["kg_to_lb"]
        elif from_unit == "g" and to_unit == "kg":
            if "g_to_kg" in self.conversion_factors:
                return value * self.conversion_factors["g_to_kg"]
            elif "kg_to_g" in self.conversion_factors:
                return value / self.conversion_factors["kg_to_g"]
        raise ValueError(f"Conversion not supported between {from_unit} and {to_unit}")
if __name__ == '__main__':
    system = WeightSystem()
    print("Initial conversion rates:")
    print(system.conversion_factors)
    system.add_conversion_factor("m_to_ft", 3.28084)
    print("\nAfter adding m_to_ft:")
    print(system.conversion_factors)
    try:
        result1 = system.convert(10, "kg", "lb")
        print(f"\n10 kg to lb: {result1:.2f} lb")
        result2 = system.convert(100, "g", "kg")
        print(f"100 g to kg: {result2:.3f} kg")
        result3 = system.convert(5, "m", "ft")
        print(f"5 m to ft: {result3:.2f} ft")
        result4 = system.convert(10, "lb", "kg")
        print(f"10 lb to kg: {result4:.3f} kg")
    except ValueError as e:
        print(f"\nError during conversion: {e}")