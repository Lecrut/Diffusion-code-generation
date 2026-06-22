def pounds_to_ounces(pounds):
    return [p * 16 for p in pounds]

def kilograms_to_ounces(kilograms):
    return [k * 35.274 for k in kilograms]

def combine_weights(pounds, kilograms):
    ounces_pounds = pounds_to_ounces(pounds)
    ounces_kilograms = kilograms_to_ounces(kilograms)
    return ounces_pounds + ounces_kilograms

if __name__ == '__main__':
    sample_pounds = [10, 20, 30]
    sample_kilograms = [5, 10, 15]
    combined_weights = combine_weights(sample_pounds, sample_kilograms)
    print(combined_weights)