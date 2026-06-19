def compare_temperatures(temp1, temp2):
    discrepancy = abs(temp1 - temp2)
    if discrepancy > 5:
        return f'Discrepancy detected: {discrepancy} degrees Celsius'
    else:
        return 'No significant discrepancy'
if __name__ == '__main__':
    temperature_value_1 = 23.5
    temperature_value_2 = 30.0
    result = compare_temperatures(temperature_value_1, temperature_value_2)
    print(result)