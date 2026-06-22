def validate_mass(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Mass must be an integer or float")

def kg_to_lb(kg):
    validate_mass(kg)
    return round(kg * 2.20462, 2)

def lb_to_kg(lb):
    validate_mass(lb)
    return round(lb / 2.20462, 2)

if __name__ == '__main__':
    print(kg_to_lb(1))
    print(lb_to_kg(2.2))