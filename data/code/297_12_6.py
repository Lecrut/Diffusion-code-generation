def convert_quantity(conversion_factors, quantity, source_unit, target_unit):
    if source_unit == target_unit:
        return quantity
    if (source_unit, target_unit) in conversion_factors:
        factor = conversion_factors[(source_unit, target_unit)]
        return quantity * factor
    else:
        raise ValueError(f"Conversion factor not found for {source_unit} to {target_unit}")
if __name__ == '__main__':
    conversion_data = {
        ('kg', 'g'): 1000.0,
        ('m', 'cm'): 100.0,
        ('liter', 'milliliter'): 1000.0,
        ('pound', 'kg'): 2.20462,
        ('meter', 'foot'): 3.28084
    }
    input_quantity = 500
    source = 'kg'
    target = 'g'
    try:
        result = convert_quantity(conversion_data, input_quantity, source, target)
        print(f"Input Quantity: {input_quantity} {source}")
        print(f"Conversion to {target}: {result} {target}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result = convert_quantity(conversion_data, 10, 'meter', 'foot')
        print(f"\nInput Quantity: 10 meter")
        print(f"Conversion to foot: {result} foot")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result = convert_quantity(conversion_data, 5, 'kg', 'liter')
        print(f"\nInput Quantity: 5 kg")
        print(f"Conversion to liter: {result} liter")
    except ValueError as e:
        print(f"Error: {e}")