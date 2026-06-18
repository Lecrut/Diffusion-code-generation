def get_mass_scale():
    constants = {
        "kg": 10**3,
        "g": 1,
        "mg": 1e-6,
        "lb": 453.59237 * 1/1000,
        "oz": 28.34952 / 1000
    }
    def convert(mass: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in constants or to_unit not in constants:
            raise ValueError("Invalid unit")
        value_in_kg = mass * constants[from_unit]
        result = value_in_kg / constants[to_unit]
        return round(result, 6)
    return convert
if __name__ == '__main__':
    scale_func = get_mass_scale()
    sample_values = [100, 500.5, -25]
    units_from = ["kg", "g"]
    units_to = ["lb", "oz"]
    for val in sample_values:
        print(f"Value {val} kg to lb:", scale_func(val, "kg", "lb"))
        print(f"Value {val} g to oz:", scale_func(val, "g", "oz"))