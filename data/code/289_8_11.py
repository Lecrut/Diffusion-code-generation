conversion_factors = {
    'lb': 0.45359237
}

def pounds_to_kilograms(pounds):
    kilograms = pounds * conversion_factors['lb']
    return f"{kilograms:.2f}"

if __name__ == '__main__':
    sample_pounds = [1, 2.5, 10]
    for pounds in sample_pounds:
        print(pounds_to_kilograms(pounds))