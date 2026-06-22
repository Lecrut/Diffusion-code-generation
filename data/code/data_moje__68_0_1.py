from decimal import Decimal, ROUND_HALF_UP

def dollars_to_cents(dollar_amount):
    if isinstance(dollar_amount, float):
        decimal_val = Decimal(str(dollar_amount))
    elif isinstance(dollar_amount, int):
        decimal_val = Decimal(dollar_amount)
    elif isinstance(dollar_amount, Decimal):
        decimal_val = dollar_amount
    else:
        raise TypeError("Unsupported type for dollar_amount")
    
    cents = decimal_val * 100
    rounded_cents = cents.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    return int(rounded_cents)

if __name__ == '__main__':
    test_values = [0.0, 1.0, 0.01, 0.99, 1.005, 1.015, 1.025, 1.035, 1.045, 1.055, 1.065, 1.075, 1.085, 1.095, 1.105, 1.115, 1.125, 1.135, 1.145, 1.155, 1.165, 1.175, 1.185, 1.195, 1.205, 1.215, 1.225, 1.235, 1.245, 1.255, 1.265, 1.275, 1.285, 1.295, 1.305, 1.315, 1.325, 1.335, 1.345, 1.355, 1.365, 1.375, 1.385, 1.395, 1.405, 1.415, 1.425, 1.435, 1.445, 1.455, 1.465, 1.475, 1.485, 1.495, 1.505, 1.515, 1.525, 1.535, 1.545, 1.555, 1.565, 1.575, 1.585, 1.595, 1.605, 1.615, 1.625, 1.635, 1.645, 1.655, 1.665, 1.675, 1.685, 1.695, 1.705, 1.715, 1.725, 1.735, 1.745, 1.755, 1.765, 1.775, 1.785, 1.795, 1.805, 1.815, 1.825, 1.835, 1.845, 1.855, 1.865, 1.875, 1.885, 1.895, 1.905, 1.915, 1.925, 1.935, 1.945, 1.955, 1.965, 1.975, 1.985, 1.995, 2.0, -1.0, -0.01, -0.99, -1.005, -1.015, 123.456, 123.454, 123.455, 123.457, 123.453, 123.452, 123.451, 123.450, 123.449, 123.448, 123.447, 123.446, 123.445, 123.444, 123.443, 123.442, 123.441, 123.440]
    
    for val in test_values:
        result = dollars_to_cents(val)
        print(result)