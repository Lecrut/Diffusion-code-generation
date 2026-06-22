def kg_to_tons(kg):
    return kg * 0.001

if __name__ == '__main__':
    sample_kg = 5000
    tons = kg_to_tons(sample_kg)
    print(f"{tons:.3f}")