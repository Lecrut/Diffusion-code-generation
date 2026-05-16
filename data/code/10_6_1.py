def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return f"Temperature 1 is warmer by {temp1 - temp2} degrees"
    elif temp2 > temp1:
        return f"Temperature 2 is warmer by {temp2 - temp1} degrees"
    else:
        return "Temperatures are equal"
if __name__ == '__main__':
    for t1, t2 in [(25, 20), (30, 25), (15, 15), (40, 35)]:
        result = compare_temperatures(t1, t2)
        print(result)