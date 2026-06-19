def compare_temperatures(temp1, temp2):
    discrepancy = abs(temp1 - temp2)
    if discrepancy > 5:
        return f'Discrepancy: {discrepancy} degrees Celsius'
    else:
        return 'No significant discrepancy'
if __name__ == '__main__':
    temperature1 = 23.5
    temperature2 = 30.0
    result = compare_temperatures(temperature1, temperature2)
    print(result)