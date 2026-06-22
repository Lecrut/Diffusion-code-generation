conversion_factor = 0.453592

def pounds_to_kilograms(pounds):
    return pounds * conversion_factor

if __name__ == '__main__':
    sample_pounds = 10
    result = pounds_to_kilograms(sample_pounds)
    print(f"{sample_pounds} pounds is {result:.2f} kilograms")