def pounds_to_kilograms(pounds):
    conversion_factor = 0.453592
    kilograms = pounds * conversion_factor
    return f"{kilograms:.2f}"

if __name__ == '__main__':
    sample_pounds = [10, 20, 30]
    for pounds in sample_pounds:
        print(pounds_to_kilograms(pounds))