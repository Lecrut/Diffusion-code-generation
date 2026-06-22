def kg_to_tons(kg):
    tons = kg * 0.001
    return round(tons, 3)

if __name__ == '__main__':
    sample_kg = 3500
    result = kg_to_tons(sample_kg)
    print(f"{sample_kg} kg is equal to {result} tons")