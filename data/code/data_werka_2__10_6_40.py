def compare_temperatures(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Both temperatures must be numbers")
    
    if temp1 > temp2:
        return "Temperature 1 is greater than Temperature 2"
    elif temp1 < temp2:
        return "Temperature 1 is less than Temperature 2"
    else:
        return "Temperatures are equal"

def test_compare_temperatures():
    assert compare_temperatures(30, 25) == "Temperature 1 is greater than Temperature 2"
    assert compare_temperatures(20, 25) == "Temperature 1 is less than Temperature 2"
    assert compare_temperatures(25, 25) == "Temperatures are equal"
    try:
        compare_temperatures("30", 25)
    except ValueError as e:
        assert str(e) == "Both temperatures must be numbers"

if __name__ == '__main__':
    test_compare_temperatures()
    print(compare_temperatures(30, 25))
    print(compare_temperatures(20, 25))
    print(compare_temperatures(25, 25))