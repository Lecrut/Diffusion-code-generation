def calculate_mean(temp1, temp2):
    if not all(isinstance(temp, (int, float)) for temp in [temp1, temp2]):
        raise ValueError("Both temperatures must be numbers")
    return round((temp1 + temp2) / 2, 2)

if __name__ == '__main__':
    sample_temp1 = 35.7
    sample_temp2 = 40.2
    mean_temperature = calculate_mean(sample_temp1, sample_temp2)
    print(mean_temperature)