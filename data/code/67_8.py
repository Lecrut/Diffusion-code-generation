def liters_to_milliliters(liters):
    return liters * 1000

def format_milliliters(milliliters):
    return f"{milliliters:.2f} milliliters"

if __name__ == '__main__':
    sample_liters = 2.5
    ml_value = liters_to_milliliters(sample_liters)
    formatted_output = format_milliliters(ml_value)
    print(formatted_output)