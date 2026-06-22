def compare_temperatures(temp1, temp2):
    return max(temp1, temp2)

if __name__ == '__main__':
    sample_temp1 = 23.5
    sample_temp2 = 19.8
    higher_temperature = compare_temperatures(sample_temp1, sample_temp2)
    print(higher_temperature)