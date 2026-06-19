def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "The first temperature is higher."
    elif temp1 < temp2:
        return "The second temperature is higher."
    else:
        return "Both temperatures are equal."

if __name__ == '__main__':
    sample_temp1 = 23.5
    sample_temp2 = 22.8
    print(compare_temperatures(sample_temp1, sample_temp2))