def kg_to_lb(kilograms):
    if kilograms is None:
        return None
    pounds = kilograms * 2.20462
    return round(pounds, 3)

if __name__ == '__main__':
    sample_kg = 10.0
    print(f"{sample_kg} kg is equal to {kg_to_lb(sample_kg):.3f} lbs")