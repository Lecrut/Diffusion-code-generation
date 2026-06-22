def celsius_to_reaumur(celsius):
    reaumur = celsius * 4 / 5
    return reaumur

if __name__ == '__main__':
    sample_celsius = -20
    converted_value = celsius_to_reaumur(sample_celsius)
    print(converted_value)