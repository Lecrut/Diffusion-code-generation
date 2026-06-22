conversion_factors = {
    'kg_to_lb': 2.20462,
}

def kg_to_pounds(kilograms):
    return kilograms * conversion_factors['kg_to_lb']

if __name__ == '__main__':
    print(kg_to_pounds(1))
    print(kg_to_pounds(5))
    print(kg_to_pounds(10))