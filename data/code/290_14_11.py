def kg_to_lb(kg):
    return round(kg * 2.20462, 2)

def lb_to_kg(lb):
    return round(lb / 2.20462, 2)

if __name__ == '__main__':
    weight_in_kg = 1.5
    weight_in_lb = 3.3

    print(f"{weight_in_kg} kg is approximately {kg_to_lb(weight_in_kg)} pounds.")
    print(f"{weight_in_lb} lb is approximately {lb_to_kg(weight_in_lb)} kilograms.")