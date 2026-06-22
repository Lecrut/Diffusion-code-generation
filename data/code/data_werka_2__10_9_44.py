def compare_temperatures(temp1, temp2):
    temperature_labels = {
        'first': "First temperature",
        'second': "Second temperature"
    }
    
    if temp1 > temp2:
        return f"{temperature_labels['first']} is higher."
    elif temp1 < temp2:
        return f"{temperature_labels['second']} is higher."
    else:
        return "Both temperatures are equal."

if __name__ == '__main__':
    sample_temp1 = 30.0
    sample_temp2 = 28.5
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)