def calculate_mean(temp1, temp2):
    return round((temp1 + temp2) / 2, 2)

if __name__ == '__main__':
    temperature1 = 30.567
    temperature2 = 25.891
    mean_temperature = calculate_mean(temperature1, temperature2)
    print(mean_temperature)