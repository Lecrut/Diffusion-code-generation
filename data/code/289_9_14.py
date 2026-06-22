LITERS_PER_MILLILITER = 0.001

def milliliters_to_liters(milliliters):
    try:
        return milliliters * LITERS_PER_MILLILITER
    except (TypeError, OverflowError) as e:
        print(f"Conversion error: {e}")
        return None

if __name__ == '__main__':
    sample_value = 1500
    result = milliliters_to_liters(sample_value)
    if result is not None:
        print(result)