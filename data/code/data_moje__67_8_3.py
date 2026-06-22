def convert_liters_to_milliliters(liters):
    return liters * 1000

def format_output(value):
    return str(value) + " milliliters"

if __name__ == '__main__':
    sample_liters = 2.5
    result = convert_liters_to_milliliters(sample_liters)
    print(format_output(result))