def kilogram_to_pound(kg):
    return round(kg * 2.20462, 2)

def pound_to_kilogram(lb):
    return round(lb / 2.20462, 2)

if __name__ == '__main__':
    print(f"1 kg is approximately {kilogram_to_pound(1)} pounds.")
    print(f"5 kg is approximately {kilogram_to_pound(5)} pounds.")
    print(f"2.2 pounds is approximately {pound_to_kilogram(2.2)} kilograms.")
    print(f"11.02 pounds is approximately {pound_to_kilogram(11.02)} kilograms.")