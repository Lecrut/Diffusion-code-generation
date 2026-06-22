def pounds_to_kilograms(pounds):
    return pounds * 0.453592

if __name__ == '__main__':
    sample_pounds = 10.0
    result_kg = pounds_to_kilograms(sample_pounds)
    print(f"{sample_pounds} lbs is {result_kg} kg")