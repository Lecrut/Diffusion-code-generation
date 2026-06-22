conversion_factor = {
    "kg_to_lb": 2.20462
}

def kg_to_lb(kilograms):
    return kilograms * conversion_factor["kg_to_lb"]

if __name__ == '__main__':
    kilograms = 1.5
    pounds = kg_to_lb(kilograms)
    print(f"{kilograms} kg is equal to {pounds:.3f} lb")