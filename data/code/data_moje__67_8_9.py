def liters_to_milliliters(liters):
    return liters * 1000

def format_output(liters, milliliters):
    return f"{liters} liters is equal to {milliliters} milliliters"

if __name__ == '__main__':
    sample_liters = 2.5
    ml = liters_to_milliliters(sample_liters)
    result = format_output(sample_liters, ml)
    print(result)