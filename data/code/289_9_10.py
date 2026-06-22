def milliliters_to_liters(ml):
    try:
        liters = ml / 1000.0
        if not isinstance(liters, (int, float)) or liters < 0:
            raise ValueError("Invalid conversion result")
        return liters
    except Exception as e:
        print(f"Error converting milliliters to liters: {e}")
        return None

if __name__ == '__main__':
    sample_ml = 1500
    result = milliliters_to_liters(sample_ml)
    print(result)