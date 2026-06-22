LITERS_TO_MILLILITERS = 1000

def convert_liters_to_milliliters(volume_in_liters):
    if not isinstance(volume_in_liters, (int, float)):
        raise TypeError("Input must be a number")
    return volume_in_liters * LITERS_TO_MILLILITERS

if __name__ == '__main__':
    sample_values = [0, 1, 2.5, -1.5, 100]
    for val in sample_values:
        result = convert_liters_to_milliliters(val)
        print(result)