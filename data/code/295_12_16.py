conversion_factor = {
    'lb': 0.453592,
}

def pounds_to_kilograms(pounds):
    return pounds * conversion_factor['lb']

if __name__ == '__main__':
    sample_pounds = 10.0
    kilograms_result = pounds_to_kilograms(sample_pounds)
    print(f"{sample_pounds} lbs is {kilograms_result:.2f} kg")