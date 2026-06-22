def kg_to_ton(kg):
    ton = kg * 0.001
    return round(ton, 3)

if __name__ == '__main__':
    sample_kg = 5000
    result = kg_to_ton(sample_kg)
    print(result)