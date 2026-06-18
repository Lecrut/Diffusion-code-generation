class LengthConverter:
    def convert_to_meters(self, value):
        if value < 0:
            raise ValueError("Length cannot be negative.")
        conversions = {
            'm': value * 1,
            'km': value * 1000,
            'cm': value / 100,
            'mm': value / 1000
        }
        return conversions['m']
    def convert_from_meters(self, meters):
        if meters < 0:
            raise ValueError("Length cannot be negative.")
        conversions = {
            'km': meters / 1000,
            'cm': meters * 100,
            'mm': meters * 1000
        }
        return list(conversions.values())
    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")
        valid_units = ['m', 'km', 'cm', 'mm']
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid unit. Must be one of {valid_units}")
        try:
            meters_in_value = self.convert_to_meters(value)
            return self._convert_from_meters(meters_in_value, to_unit)
        except (ValueError, TypeError):
            raise
if __name__ == '__main__':
    converter = LengthConverter()
    sample_values = [10]          
    for val in sample_values:
        print(f"Converting {val} m to other units:")
        try:
            km_value = converter.convert(val, 'm', 'km')
            cm_value = converter.convert(val, 'm', 'cm')
            mm_value = converter.convert(val, 'm', 'mm')
            print(f"  {val} m -> {km_value:.2f} km")
            print(f"  {val} m -> {cm_value:.2f} cm")
            print(f"  {val} m -> {mm_value:.2f} mm")
        except Exception as e:
            print(f"Error during conversion: {e}")
    try:
        converter.convert(-5, 'm', 'km')
    except ValueError:
        pass
    test_km = 0.01
    result_meters = converter.convert_from_meters(test_km * 1000)[0]
    print(f"Converted {test_km} km back to meters: {result_meters}")