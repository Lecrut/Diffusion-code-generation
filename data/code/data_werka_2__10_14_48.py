def compare_temperatures(temp1, temp2):
    temperature_map = {'temp1': temp1, 'temp2': temp2}
    return max(temperature_map.values())

if __name__ == '__main__':
    sample_temp1 = 29.0
    sample_temp2 = 31.5
    higher_temperature = compare_temperatures(sample_temp1, sample_temp2)
    print(higher_temperature)