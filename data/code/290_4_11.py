conversion_factor = {
    'pounds': 0.453592
}

def convert_pounds_to_kilograms(weight):
    if weight < 0:
        raise ValueError("Weight cannot be negative")
    return round(weight * conversion_factor['pounds'], 1)

if __name__ == '__main__':
    sample_weight = -5
    try:
        result_weight = convert_pounds_to_kilograms(sample_weight)
        print(result_weight)
    except ValueError as e:
        print(e)