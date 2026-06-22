def kg_to_pounds(kilograms):
    return kilograms * 2.20462

if __name__ == '__main__':
    sample_values = [1, 5, 10, 100]
    print("--- Kilograms to Pounds Conversion Example ---")
    for kg in sample_values:
        pounds = kg_to_pounds(kg)
        print(f"{kg} kg is equal to {pounds:.2f} lbs")