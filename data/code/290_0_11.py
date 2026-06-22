CONVERSION_FACTOR = 2.20462

def kg_to_lb(kilograms):
    return kilograms * CONVERSION_FACTOR

if __name__ == '__main__':
    print(f"5 kg is equal to {kg_to_lb(5)} lb")
    print(f"10 kg is equal to {kg_to_lb(10)} lb")
    print(f"2.5 kg is equal to {kg_to_lb(2.5)} lb")