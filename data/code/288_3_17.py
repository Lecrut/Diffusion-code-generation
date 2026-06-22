def celsius_to_reaumur(celsius):
    return celsius * 4 / 5

if __name__ == '__main__':
    sample_celsius = 20.0
    reaumur = celsius_to_reaumur(sample_celsius)
    print(reaumur)