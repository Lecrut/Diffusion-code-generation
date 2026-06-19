def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "First temperature is higher"
    elif temp1 < temp2:
        return "Second temperature is higher"
    else:
        return "Temperatures are equal"

def test_compare_temperatures():
    assert compare_temperatures(30, 25) == "First temperature is higher"
    assert compare_temperatures(20, 25) == "Second temperature is higher"
    assert compare_temperatures(25, 25) == "Temperatures are equal"

if __name__ == '__main__':
    test_compare_temperatures()
    print(compare_temperatures(30, 25))
    print(compare_temperatures(20, 25))
    print(compare_temperatures(25, 25))