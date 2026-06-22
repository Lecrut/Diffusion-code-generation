def pounds_to_kilograms(pounds):
    return pounds * 0.453592

def kilograms_to_pounds(kilograms):
    return kilograms / 0.453592

if __name__ == '__main__':
    sample_pounds = 10
    sample_kilograms = 5
    
    print(f"{sample_pounds} pounds is {pounds_to_kilograms(sample_pounds):.2f} kilograms")
    print(f"{sample_kilograms} kilograms is {kilograms_to_pounds(sample_kilograms):.2f} pounds")