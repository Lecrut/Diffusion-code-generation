def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return f"Temperature 1 is warmer by {temp1 - temp2} degrees"
    elif temp2 > temp1:
        return f"Temperature 2 is warmer by {temp2 - temp1} degrees"
    else:
        return "Temperatures are equal"
if __name__ == '__main__':
    temp_a = 25
    temp_b = 20
    for result in compare_temperatures(temp_a, temp_b):
        print(result)
    temp_c = 30
    temp_d = 30
    for result in compare_temperatures(temp_c, temp_d):
        print(result)
    temp_e = 22
    temp_f = 28
    for result in compare_temperatures(temp_e, temp_f):
        print(result)