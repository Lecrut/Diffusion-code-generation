def calculate_temperature_difference(temp1, temp2):
    if temp1 > temp2:
        return temp1 - temp2
    else:
        return temp2 - temp1
if __name__ == '__main__':
    t1 = 30
    t2 = 20
    difference1 = calculate_temperature_difference(t1, t2)
    print(f"Difference between {t1} and {t2}: {difference1}")
    t3 = 15
    t4 = 45
    difference2 = calculate_temperature_difference(t3, t4)
    print(f"Difference between {t3} and {t4}: {difference2}")