def kg_to_pounds(kg):
    return kg * 2.20462

if __name__ == '__main__':
    kilograms = 7.5
    pounds = kg_to_pounds(kilograms)
    print(f"{kilograms} kg is equal to {pounds:.2f} lb")