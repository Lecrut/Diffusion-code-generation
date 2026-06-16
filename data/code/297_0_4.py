import math
def convert_length(value, from_unit, to_unit):
    if from_unit == 'm':
        if to_unit == 'km':
            return value / 1000
        elif to_unit == 'ft':
            return value * 3.28084
        elif to_unit == 'mi':
            return value / 1609.34
    elif from_unit == 'km':
        if to_unit == 'm':
            return value * 1000
        elif to_unit == 'ft':
            return value * 3280.84
        elif to_unit == 'mi':
            return value
    elif from_unit == 'ft':
        if to_unit == 'm':
            return value / 3.28084
        elif to_unit == 'km':
            return value / 1609.34
        elif to_unit == 'mi':
            return value / 1609.34
    elif from_unit == 'mi':
        if to_unit == 'km':
            return value * 1.60934
        elif to_unit == 'ft':
            return value * 5280
        elif to_unit == 'mi':
            return value
    return None
def convert_mass(value, from_unit, to_unit):
    if from_unit == 'g':
        if to_unit == 'kg':
            return value / 1000
        elif to_unit == 'lb':
            return value * 0.00220462
        elif to_unit == 'oz':
            return value * 0.0352739
    elif from_unit == 'kg':
        if to_unit == 'g':
            return value * 1000
        elif to_unit == 'lb':
            return value * 2.20462
        elif to_unit == 'oz':
            return value * 35.2739
    elif from_unit == 'lb':
        if to_unit == 'kg':
            return value / 2.20462
        elif to_unit == 'g':
            return value * 453.592
        elif to_unit == 'oz':
            return value * 453.592
    elif from_unit == 'oz':
        if to_unit == 'lb':
            return value / 16
        elif to_unit == 'kg':
            return value * 0.000283495
        elif to_unit == 'g':
            return value * 28.3495
    return None
if __name__ == '__main__':
    print("--- Length Conversions ---")
    m_val = 10
    ft_result = convert_length(m_val, 'm', 'ft')
    print(f"{m_val} meters is equal to {ft_result:.4f} feet")
    km_val = 50
    mi_result = convert_length(km_val, 'km', 'mi')
    print(f"{km_val} kilometers is equal to {mi_result:.4f} miles")
    ft_val = 100
    m_result = convert_length(ft_val, 'ft', 'm')
    print(f"{ft_val} feet is equal to {m_result:.4f} meters")
    print("\n--- Mass Conversions ---")
    g_val = 500
    kg_result = convert_mass(g_val, 'g', 'kg')
    print(f"{g_val} grams is equal to {kg_result:.4f} kilograms")
    lb_val = 10
    oz_result = convert_mass(lb_val, 'lb', 'oz')
    print(f"{lb_val} pounds is equal to {oz_result:.4f} ounces")
    kg_val = 2.5
    lb_result = convert_mass(kg_val, 'kg', 'lb')
    print(f"{kg_val} kilograms is equal to {lb_result:.4f} pounds")