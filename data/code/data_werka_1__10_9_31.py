def calculate_mean(temp1, temp2):
    return round((temp1 + temp2) / 2, 2)

if __name__ == '__main__':
    temp_reading1 = 98.6
    temp_reading2 = 100.4
    mean_temperature = calculate_mean(temp_reading1, temp_reading2)
    print(mean_temperature)