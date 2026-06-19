def calculate_mean(temp1, temp2):
    return round((temp1 + temp2) / 2, 2)

if __name__ == '__main__':
    sample_temp1 = 30.5678
    sample_temp2 = 25.4321
    mean_temperature = calculate_mean(sample_temp1, sample_temp2)
    print(mean_temperature)