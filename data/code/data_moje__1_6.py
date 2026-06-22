class Weight:
    def __init__(self, value, unit="kg"):
        if unit.lower() not in ("kg", "lbs", "lb", "pounds", "kilograms"):
            raise ValueError(f"Unsupported unit: {unit}")
        self.unit = unit.lower()
        self.value = float(value)

    def convert(self, target_unit):
        if target_unit.lower() not in ("kg", "lbs", "lb", "pounds", "kilograms"):
            raise ValueError(f"Unsupported target unit: {target_unit}")

        target_unit = target_unit.lower()
        if target_unit in ("lbs", "lb", "pounds"):
            target_unit = "lbs"
        else:
            target_unit = "kg"

        current_unit = self.unit
        if current_unit in ("lbs", "lb", "pounds"):
            current_unit = "lbs"
        else:
            current_unit = "kg"

        value_in_kg = self.value
        if current_unit == "lbs":
            value_in_kg = self.value * 0.453592

        if target_unit == "lbs":
            new_value = value_in_kg / 0.453592
        else:
            new_value = value_in_kg

        return Weight(new_value, target_unit)

    def __repr__(self):
        return f"Weight(value={self.value:.4f}, unit={self.unit})"

if __name__ == "__main__":
    w1 = Weight(100, "lbs")
    w2 = w1.convert("kg")
    print(w2)

    w3 = Weight(50, "kg")
    w4 = w3.convert("lbs")
    print(w4)

    w5 = Weight(10, "lbs")
    w6 = w5.convert("kg")
    w7 = w6.convert("lbs")
    print(w7)