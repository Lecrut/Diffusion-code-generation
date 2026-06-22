def kg_to_lb(kg):
    if not isinstance(kg, (int, float)) or kg < 0:
        raise ValueError("Invalid input: kilograms must be a non-negative number")
    return round(kg * 2.20462, 2)

def lb_to_kg(lb):
    if not isinstance(lb, (int, float)) or lb < 0:
        raise ValueError("Invalid input: pounds must be a non-negative number")
    return round(lb / 2.20462, 2)

if __name__ == '__main__':
    print(kg_to_lb(1))
    print(lb_to_kg(2.2))