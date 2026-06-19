def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        yield f"T1 is warmer by {temp1 - temp2} degrees"
    elif temp2 > temp1:
        yield f"T2 is warmer by {temp2 - temp1} degrees"
    else:
        yield "Both temperatures are equal"

if __name__ == '__main__':
    temperature1 = 75
    temperature2 = 60
    for result in compare_temperatures(temperature1, temperature2):
        print(result)