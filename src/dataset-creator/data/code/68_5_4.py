class VolumeConverter:
    def __init__(self):
        self._registry = {}
    def register_unit(self, name, factor_to_base):
        if not isinstance(factor_to_base, (int, float)):
            raise ValueError("Factor must be a number")
        self._registry[name] = factor_to_base
    def convert_from(self, value: float, from_unit: str) -> dict:
        if from_unit.lower() not in [u.lower() for u in self._registry]:
            available = list(self._registry.keys())
            raise ValueError(f"Unknown unit '{from_unit}'. Available units: {available}")
        base_value = value * self._registry[from_unit]
        return {"base": round(base_value, 6)}
    def convert_to(self, value: float, to_unit: str) -> dict:
        if to_unit.lower() not in [u.lower() for u in self._registry]:
            available = list(self._registry.keys())
            raise ValueError(f"Unknown unit '{to_unit}'. Available units: {available}")
        base_value = value * self._registry["base"] / self._registry[to_unit] if "base" in self._registry else 0.0
        return {"target": round(base_value, 6)}
def main():
    converter = VolumeConverter()
    converter.register_unit("liter", 1)
    converter.register_unit("gallon_usa", 3.785412)
    result_from_liter = converter.convert_from(10, "liter")
    print(f"Converted from liter: {result_from_liter}")
    result_to_gallon = converter.convert_to(10, "gallon_usa")
    print(f"Converted to gallon_usa: {result_to_gallon}")
if __name__ == '__main__':
    main()