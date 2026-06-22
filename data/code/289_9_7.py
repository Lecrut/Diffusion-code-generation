def ml_to_l(ml):
    try:
        l = ml / 1000
        return l
    except OverflowError:
        print("Overflow error occurred")
        return None

if __name__ == '__main__':
    sample_ml = 2500
    result = ml_to_l(sample_ml)
    if result is not None:
        print(f"{sample_ml} milliliters is {result} liters")