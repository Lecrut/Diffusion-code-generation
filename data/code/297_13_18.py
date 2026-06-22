POUNDS_TO_KILOGRAMS = 0.453592
KILOGRAMS_TO_POUNDS = 1 / POUNDS_TO_KILOGRAMS

def pounds_to_kilograms(pounds):
    return pounds * POUNDS_TO_KILOGRAMS

def kilograms_to_pounds(kilograms):
    return kilograms * KILOGRAMS_TO_POUNDS
if __name__ == '__main__':
    pounds_value = 10
    kilograms_value = 5
    kg_result = pounds_to_kilograms(pounds_value)
    print(f'{pounds_value} pounds is equal to {kg_result} kilograms')
    lb_result = kilograms_to_pounds(kilograms_value)
    print(f'{kilograms_value} kilograms is equal to {lb_result} pounds')