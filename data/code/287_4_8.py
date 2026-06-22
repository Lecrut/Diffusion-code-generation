def convert_and_combine_weights(pounds, kilograms):
    ounces_per_pound = 16
    ounces_per_kg = 35.274

    pounds_in_ounces = [weight * ounces_per_pound for weight in pounds]
    kg_in_ounces = [weight * ounces_per_kg for weight in kilograms]

    combined_weights = pounds_in_ounces + kg_in_ounces
    return combined_weights

if __name__ == '__main__':
    sample_pounds = [10, 20, 30]
    sample_kilograms = [5, 10, 15]
    result = convert_and_combine_weights(sample_pounds, sample_kilograms)
    print(result)