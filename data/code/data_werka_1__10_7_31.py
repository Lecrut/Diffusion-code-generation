def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "First temperature is greater"
    elif temp1 < temp2:
        return "Second temperature is greater"
    else:
        return "Temperatures are equal"

def test_compare_temperatures():
    assert compare_temperatures(30, 25) == "First temperature is greater"
    assert compare_temperatures(20, 25) == "Second temperature is greater"
    assert compare_temperatures(15, 15) == "Temperatures are equal"

if __name__ == '__main__':
    sample_temp1 = 35
    sample_temp2 = 40
    result = compare_temperatures(sample_temp1, sample_temp2)
    print(result)