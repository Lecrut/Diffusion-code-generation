def pounds_to_kilograms(pounds):
    if not isinstance(pounds, (int, float)):
        raise ValueError("Input must be a number.")
    kilograms = pounds * 0.453592
    return f"{kilograms:.2f}"

if __name__ == '__main__':
    sample_pounds = [10, 20, 30]
    for pounds in sample_pounds:
        print(pounds_to_kilograms(pounds))