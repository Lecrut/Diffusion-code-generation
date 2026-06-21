def validate_temperature(temp):
    if not isinstance(temp, (int, float)):
        raise ValueError("Temperature must be an integer or float")

def compare_temperatures(temp1, temp2):
    validate_temperature(temp1)
    validate_temperature(temp2)
    
    if temp1 > temp2:
        return "First temperature is higher than the second"
    elif temp1 < temp2:
        return "First temperature is lower than the second"
    else:
        return "Both temperatures are equal"

def test_compare_temperatures():
    assert compare_temperatures(30, 25) == "First temperature is higher than the second"
    assert compare_temperatures(20, 25) == "First temperature is lower than the second"
    assert compare_temperatures(25, 25) == "Both temperatures are equal"

if __name__ == '__main__':
    test_compare_temperatures()
    print(compare_temperatures(35, 40))
    print(compare_temperatures(15, 10))
    print(compare_temperatures(20, 20))