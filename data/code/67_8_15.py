def liters_to_milliliters(liters):
    return liters * 1000

def format_output(value):
    return str(value) + " milliliters"

if __name__ == '__main__':
    sample_liters = 2.5
    converted_value = liters_to_milliliters(sample_liters)
    formatted_result = format_output(converted_value)
    print(formatted_result)