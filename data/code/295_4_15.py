CONVERSION_FACTOR = 2.20462

def kg_to_lb(kg):
    return round(kg * CONVERSION_FACTOR, 3)

if __name__ == '__main__':
    sample_kg = 1.0
    print(f"{sample_kg} kg is equal to {kg_to_lb(sample_kg)} lb")