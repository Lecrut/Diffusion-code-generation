KG_TO_TONS = 0.001

def kg_to_tons(kg):
    return round(kg * KG_TO_TONS, 3)

if __name__ == '__main__':
    sample_kg = 2500
    tons = kg_to_tons(sample_kg)
    print(f"{tons} tons")