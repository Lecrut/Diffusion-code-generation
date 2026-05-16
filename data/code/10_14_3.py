def calculate_temperature_difference(temp1, temp2):
    if temp1 > temp2:
        return temp1 - temp2
    else:
        return temp2 - temp1
if __name__ == '__main__':
    t1 = 30
    t2 = 45
    difference = calculate_temperature_difference(t1, t2)
    print(difference)