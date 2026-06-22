def calculate_mean(temp1, temp2):
    return round((temp1 + temp2) / 2, 2)

if __name__ == '__main__':
    temp_reading1 = 23.567
    temp_reading2 = 25.432
    mean_temperature = calculate_mean(temp_reading1, temp_reading2)
    print(mean_temperature)