def ml_to_lit(ml):
    try:
        return ml / 1000.0
    except OverflowError:
        print("Overflow error occurred.")
        return None

if __name__ == '__main__':
    sample_ml = 2500
    result = ml_to_lit(sample_ml)
    if result is not None:
        print(f"{sample_ml} milliliters is {result} liters")