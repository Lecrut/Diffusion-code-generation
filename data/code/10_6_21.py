def compare_temperatures(temp1, temp2):
    difference = abs(temp1 - temp2)
    if temp1 > temp2:
        return f"{temp1} is higher than {temp2} by {difference}"
    elif temp1 < temp2:
        return f"{temp2} is higher than {temp1} by {difference}"
    else:
        return "Both temperatures are equal"

if __name__ == '__main__':
    sample_temp1 = 30
    sample_temp2 = 25
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)