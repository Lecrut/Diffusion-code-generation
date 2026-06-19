def compare_temperatures(temp1, temp2):
    discrepancy = abs(temp1 - temp2)
    if discrepancy > 5:
        return f"Discrepancy detected: {discrepancy} degrees Celsius"
    else:
        return "No significant discrepancy"

if __name__ == '__main__':
    temp_value1 = 20.5
    temp_value2 = 30.0
    result = compare_temperatures(temp_value1, temp_value2)
    print(result)