def compare_temperatures(temp1, temp2):
    temperature_messages = {
        1: "First temperature is higher.",
        -1: "Second temperature is higher.",
        0: "Both temperatures are equal."
    }
    
    comparison_result = (temp1 > temp2) - (temp1 < temp2)
    return temperature_messages[comparison_result]

if __name__ == '__main__':
    sample_temp1 = 30.0
    sample_temp2 = 27.5
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)