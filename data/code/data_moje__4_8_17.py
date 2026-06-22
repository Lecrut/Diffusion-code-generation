class DistanceConverter:
    CONVERSION_FACTOR = 1.609344

    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit.lower().strip()
        if self.unit not in ('km', 'miles', 'kilometers', 'mi'):
            raise ValueError("Unit must be 'km', 'kilometers', 'miles', or 'mi'.")

    def _normalize_unit(self, unit: str) -> str:
        u = unit.lower().strip()
        if u in ('km', 'kilometers'):
            return 'km'
        if u in ('miles', 'mi'):
            return 'miles'
        raise ValueError("Unit must be 'km', 'kilometers', 'miles', or 'mi'.")

    def convert_to_kilometers(self) -> float:
        target = self._normalize_unit('kilometers')
        if self.unit == 'miles' or self.unit == 'mi':
            return self.value * self.CONVERSION_FACTOR
        return self.value

    def convert_to_miles(self) -> float:
        target = self._normalize_unit('miles')
        if self.unit == 'km' or self.unit == 'kilometers':
            return self.value / self.CONVERSION_FACTOR
        return self.value

    def get_formatted_result(self, target_unit_name: str) -> str:
        normalized_target = target_unit_name.lower().strip()
        is_km_target = normalized_target in ('km', 'kilometers')
        is_mi_target = normalized_target in ('miles', 'mi')
        
        if not is_km_target and not is_mi_target:
            raise ValueError("Target unit must be 'km', 'kilometers', 'miles', or 'mi'.")
        
        result_value = self.convert_to_kilometers() if is_km_target else self.convert_to_miles()
        final_unit_label = "kilometers" if is_km_target else "miles"
        
        return f"{self.value} {self.unit} is equal to {result_value:.4f} {final_unit_label}"

if __name__ == '__main__':
    converter_1 = DistanceConverter(100.0, 'km')
    result_1 = converter_1.get_formatted_result('miles')
    print(result_1)
    
    converter_2 = DistanceConverter(50.0, 'miles')
    result_2 = converter_2.get_formatted_result('km')
    print(result_2)