def validate_input(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError('Input value must be a number.')
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError('Units must be provided as strings.')
    if from_unit == to_unit:
        return value

def convert_kg_to_lb(kg):
    return kg * 2.2046226218

def convert_lb_to_kg(lb):
    return lb / 2.2046226218

def convert_kg_to_g(kg):
    return kg * 1000.0

def convert_g_to_kg(g):
    return g / 1000.0

def convert_lb_to_g(lb):
    return lb * 453.592

def convert_g_to_lb(g):
    return g / 453.592
if __name__ == '__main__':
    print(convert_kg_to_lb(1))
    print(convert_lb_to_kg(2.2046226218))
    print(convert_kg_to_g(1))
    print(convert_g_to_kg(1000.0))
    print(convert_lb_to_g(2.2046226218))
    print(convert_g_to_lb(999.9971350000001))