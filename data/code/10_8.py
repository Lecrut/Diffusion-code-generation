def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "temp1 is greater"
    elif temp1 < temp2:
        return "temp1 is less"
    else:
        return "temperatures are equal"
def test_compare_temperatures():
    assert compare_temperatures(30, 20) == "temp1 is greater"
    assert compare_temperatures(15, 30) == "temp1 is less"
    assert compare_temperatures(25, 25) == "temperatures are equal"
    assert compare_temperatures(100, 50) == "temp1 is greater"
    assert compare_temperatures(5, 10) == "temp1 is less"
if __name__ == '__main__':
    test_compare_temperatures()