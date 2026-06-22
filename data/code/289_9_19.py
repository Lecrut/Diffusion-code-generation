CONVERSION_FACTOR = 1e-3

def convert_milliliters_to_liters(milliliters):
    try:
        return milliliters * CONVERSION_FACTOR
    except (OverflowError, ValueError) as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    value = 1500.5
    result = convert_milliliters_to_liters(value)
    print(result)