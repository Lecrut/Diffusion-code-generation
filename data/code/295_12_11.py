CONVERSION_FACTOR = 0.453592

def pounds_to_kilograms(pounds):
    return pounds * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_pounds = 100.0
    kilograms_result = pounds_to_kilograms(sample_pounds)
    print(f"{sample_pounds} lbs is {kilograms_result} kg")