def liters_to_milliliters(liters):
    return liters * 1000

def format_output(liters, milliliters):
    return f"{liters} liters is equal to {milliliters} milliliters"

if __name__ == "__main__":
    sample_liters = 2.5
    result_ml = liters_to_milliliters(sample_liters)
    print(format_output(sample_liters, result_ml))