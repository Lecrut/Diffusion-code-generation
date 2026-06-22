def compare_temperatures(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Both temperatures must be numbers")
    
    if temp1 > temp2:
        return "Temperature 1 is higher"
    elif temp1 < temp2:
        return "Temperature 1 is lower"
    else:
        return "Temperatures are equal"

def test_compare_temperatures():
    assert compare_temperatures(30, 25) == "Temperature 1 is higher"
    assert compare_temperatures(20, 25) == "Temperature 1 is lower"
    assert compare_temperatures(25, 25) == "Temperatures are equal"
    try:
        compare_temperatures('30', 25)
    except ValueError as e:
        assert str(e) == "Both temperatures must be numbers"

if __name__ == '__main__':
    test_compare_temperatures()
    print(compare_temperatures(30, 25))
    print(compare_temperatures(20, 25))
    print(compare_temperatures(25, 25))
    try:
        print(compare_temperatures('30', 25))
    except ValueError as e:
        print(e)