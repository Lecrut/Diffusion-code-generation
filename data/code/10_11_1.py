def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "Temperature 1 is higher"
    elif temp1 < temp2:
        return "Temperature 2 is higher"
    else:
        return "Temperatures are equal"
if __name__ == '__main__':
    t1 = 25.5
    t2 = 25.5
    print(f"Comparing {t1} and {t2}: {compare_temperatures(t1, t2)}")
    t3 = 30
    t4 = 22
    print(f"Comparing {t3} and {t4}: {compare_temperatures(t3, t4)}")
    t5 = 15
    t6 = 18.7
    print(f"Comparing {t5} and {t6}: {compare_temperatures(t5, t6)}")