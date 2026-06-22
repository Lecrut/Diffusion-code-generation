def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "temp1 is greater than temp2"
    elif temp1 < temp2:
        return "temp1 is less than temp2"
    else:
        return "temp1 is equal to temp2"

def test_compare_temperatures():
    assert compare_temperatures(30, 25) == "temp1 is greater than temp2"
    assert compare_temperatures(20, 25) == "temp1 is less than temp2"
    assert compare_temperatures(25, 25) == "temp1 is equal to temp2"

if __name__ == '__main__':
    print(compare_temperatures(30, 25))
    print(compare_temperatures(20, 25))
    print(compare_temperatures(25, 25))