def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "Temperature 1 is higher"
    elif temp1 < temp2:
        return "Temperature 2 is higher"
    else:
        return "Temperatures are equal"
if __name__ == '__main__':
    print(compare_temperatures(25.5, 20.0))
    print(compare_temperatures(30, 30))
    print(compare_temperatures(15, 45))
    print(compare_temperatures(100, 99.9))