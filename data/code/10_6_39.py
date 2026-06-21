def compare_temperatures(temp1, temp2):
    comparison_map = {
        1: "Temperature 1 is higher",
        -1: "Temperature 1 is lower",
        0: "Temperatures are equal"
    }
    result_key = (temp1 > temp2) - (temp1 < temp2)
    return comparison_map[result_key]

def test_compare_temperatures():
    assert compare_temperatures(30, 25) == "Temperature 1 is higher"
    assert compare_temperatures(20, 25) == "Temperature 1 is lower"
    assert compare_temperatures(25, 25) == "Temperatures are equal"

if __name__ == '__main__':
    test_compare_temperatures()
    print(compare_temperatures(30, 25))
    print(compare_temperatures(20, 25))
    print(compare_temperatures(25, 25))