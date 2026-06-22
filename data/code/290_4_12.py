def convert_pounds_to_kilograms(pounds):
    if pounds < 0:
        raise ValueError("Weight cannot be negative")
    return round(pounds * 0.453592, 1)

if __name__ == '__main__':
    sample_weight = 150
    result_weight = convert_pounds_to_kilograms(sample_weight)
    print(result_weight)