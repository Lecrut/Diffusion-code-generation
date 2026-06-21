def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        result = "First temperature is greater than the second"
    elif temp1 < temp2:
        result = "First temperature is less than the second"
    else:
        result = "Both temperatures are equal"
    return result

def test_compare_temperatures():
    assert compare_temperatures(30, 25) == "First temperature is greater than the second"
    assert compare_temperatures(20, 25) == "First temperature is less than the second"
    assert compare_temperatures(25, 25) == "Both temperatures are equal"

if __name__ == '__main__':
    test_compare_temperatures()
    
    temp1 = 35
    temp2 = 40
    comparison_result = compare_temperatures(temp1, temp2)
    print(comparison_result)

    temp1 = 18
    temp2 = 18
    comparison_result = compare_temperatures(temp1, temp2)
    print(comparison_result)

    temp1 = 27
    temp2 = 30
    comparison_result = compare_temperatures(temp1, temp2)
    print(comparison_result)