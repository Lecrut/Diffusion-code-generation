conversion_factor = {'pounds': 0.45359237}

def pounds_to_kilograms(pounds):
    if pounds < 0:
        return "Invalid input: weight cannot be negative."
    elif pounds == 0:
        return 0.0
    else:
        kilograms = pounds * conversion_factor['pounds']
        return round(kilograms, 1)

if __name__ == '__main__':
    sample_weights_pounds = [0, 1500, 2500.5, -100]
    for weight in sample_weights_pounds:
        result_kilograms = pounds_to_kilograms(weight)
        print(f"{weight} pounds is {result_kilograms} kilograms")