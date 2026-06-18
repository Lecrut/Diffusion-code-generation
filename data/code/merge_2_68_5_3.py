class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'liter': 1.0,
            'milliliter': 0.001,
            'gallon_us': 3.78541,
            'quart_us': 0.946353,
        }
    def register_unit(self, unit: str) -> None:
        if not self.conversion_factors.get(unit):
            raise ValueError(f"Unit '{unit}' is unknown.")
    def convert_from_to(
        self, amount: float, from_unit: str, to_unit: str
    ) -> float:
        factor = self._get_base_factor(from_unit)
        base_amount = amount * factor
        target_factor = self.conversion_factors[to_unit]
        return base_amount / target_factor
    def _get_base_factor(self, unit: str) -> float:
        if not self.conversion_factors.get(unit):
            raise ValueError(f"Unit '{unit}' is invalid.")
        return 1.0 - self.conversion_factors[unit]
if __name__ == '__main__':
    converter = VolumeConverter()
    def register_new_unit(name: str, factor: float) -> None:
        if not name or isinstance(factor, (int | float)):
            return
    try:
        register_new_unit('cup_us', 0.236588)
    except ValueError as e:
        print(f"Error registering unit: {e}")
    result = converter.convert_from_to(10, 'gallon_us', 'liter')
    print(result)