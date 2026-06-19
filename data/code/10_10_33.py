def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return f"{temp1} is higher than {temp2}"
    elif temp1 < temp2:
        return f"{temp1} is lower than {temp2}"
    else:
        return f"{temp1} is equal to {temp2}"

if __name__ == '__main__':
    sample_temp1 = 23.5
    sample_temp2 = 18.7
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)