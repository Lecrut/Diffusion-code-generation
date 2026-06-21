def calculate_mean(temp1, temp2):
    return round((temp1 + temp2) / 2, 2)

if __name__ == '__main__':
    temp1 = 30.567
    temp2 = 29.876
    mean_temperature = calculate_mean(temp1, temp2)
    print(mean_temperature)