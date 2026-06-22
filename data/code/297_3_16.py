CONVERSION_FACTOR = 0.453592

def pounds_to_kilograms(pounds):
    return pounds * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_pounds = 160
    result_kg = pounds_to_kilograms(sample_pounds)
    print(result_kg)