conversion_factor = 2.20462

def kg_to_lb(kg):
    return round(kg * conversion_factor, 2)

def lb_to_kg(lb):
    return round(lb / conversion_factor, 2)

if __name__ == '__main__':
    print(f"1 kg is approximately {kg_to_lb(1)} pounds.")
    print(f"5 kg is approximately {kg_to_lb(5)} pounds.")
    print(f"2.2 pounds is approximately {lb_to_kg(2.2)} kilograms.")
    print(f"11.02 pounds is approximately {lb_to_kg(11.02)} kilograms.")