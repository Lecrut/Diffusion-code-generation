def convert_quantity(conversion_factors, quantity, source_unit, target_unit):
    if source_unit == target_unit:
        return quantity
    if source_unit not in conversion_factors or target_unit not in conversion_factors:
        raise ValueError("One or both units are not defined in the conversion factors.")
    if (source_unit, target_unit) in conversion_factors:
        return quantity * conversion_factors[(source_unit, target_unit)]
    raise ValueError(f"Conversion from {source_unit} to {target_unit} is not directly defined.")
if __name__ == '__main__':
    conversion_data = {
        ('meters', 'feet'): 3.28084,
        ('kilograms', 'pounds'): 2.20462,
        ('liters', 'gallons'): 3.78541,
        ('miles', 'kilometers'): 1.60934,
    }
    quantity_to_convert = 10
    print(f"--- Conversion Test ---")
    try:
        result1 = convert_quantity(conversion_data, quantity_to_convert, 'meters', 'feet')
        print(f"{quantity_to_convert} meters is equal to {result1:.4f} feet.")
        result2 = convert_quantity(conversion_data, quantity_to_convert, 'kilograms', 'pounds')
        print(f"{quantity_to_convert} kilograms is equal to {result2:.4f} pounds.")
        result3 = convert_quantity(conversion_data, quantity_to_convert, 'liters', 'gallons')
        print(f"{quantity_to_convert} liters is equal to {result3:.4f} gallons.")
        try:
            convert_quantity(conversion_data, quantity_to_convert, 'meters', 'kilograms')
        except ValueError as e:
            print(f"\nError caught successfully: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")