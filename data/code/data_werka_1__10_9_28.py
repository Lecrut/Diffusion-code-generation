def calculate_mean(temp1, temp2):
    return round((temp1 + temp2) / 2, 2)

if __name__ == '__main__':
    sample_temp1 = 72.5
    sample_temp2 = 68.3
    mean_temperature = calculate_mean(sample_temp1, sample_temp2)
    print(mean_temperature)