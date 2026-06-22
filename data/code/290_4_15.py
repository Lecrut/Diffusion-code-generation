conversion_factor = {
    'pounds_to_kilograms': 0.45359237
}

def convert_pounds_to_kilograms(pounds):
    if pounds < 0:
        return "Invalid input: Negative weight"
    elif pounds == 0:
        return 0.0
    else:
        kilograms = pounds * conversion_factor['pounds_to_kilograms']
        return round(kilograms, 1)

if __name__ == '__main__':
    sample_weights_pounds = [0, -5, 10, 25]
    for weight in sample_weights_pounds:
        result_weight_kg = convert_pounds_to_kilograms(weight)
        print(f"{weight} pounds is {result_weight_kg} kilograms")