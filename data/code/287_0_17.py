CONVERSION_FACTOR = 2.20462

def kg_to_lbs(kilograms):
    return kilograms * CONVERSION_FACTOR
if __name__ == '__main__':
    print(kg_to_lbs(1))
    print(kg_to_lbs(5))
    print(kg_to_lbs(10))