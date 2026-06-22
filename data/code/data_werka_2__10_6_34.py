def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "Temp1 is greater than Temp2"
    elif temp1 < temp2:
        return "Temp1 is less than Temp2"
    else:
        return "Temp1 is equal to Temp2"

def test_compare_temperatures():
    assert compare_temperatures(30, 25) == "Temp1 is greater than Temp2"
    assert compare_temperatures(20, 25) == "Temp1 is less than Temp2"
    assert compare_temperatures(25, 25) == "Temp1 is equal to Temp2"

if __name__ == '__main__':
    test_compare_temperatures()
    print(compare_temperatures(30, 25))
    print(compare_temperatures(20, 25))
    print(compare_temperatures(25, 25))