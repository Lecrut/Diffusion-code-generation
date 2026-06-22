def kg_to_tons(kg):
    if not isinstance(kg, (int, float)) or kg < 0:
        raise ValueError("Input must be a non-negative number")
    return round(kg * 0.001, 3)

if __name__ == '__main__':
    sample_kg = 2500
    result = kg_to_tons(sample_kg)
    print(f"{result} tons")