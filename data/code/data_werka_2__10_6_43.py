def compare_temperatures(temp1, temp2):
    comparison_map = {
        1: "First temperature is greater than the second",
        -1: "First temperature is less than the second",
        0: "Both temperatures are equal"
    }
    if temp1 > temp2:
        return comparison_map[1]
    elif temp1 < temp2:
        return comparison_map[-1]
    else:
        return comparison_map[0]

def test_compare_temperatures():
    assert compare_temperatures(30, 25) == "First temperature is greater than the second"
    assert compare_temperatures(20, 25) == "First temperature is less than the second"
    assert compare_temperatures(25, 25) == "Both temperatures are equal"

if __name__ == '__main__':
    test_compare_temperatures()
    print(compare_temperatures(30, 25))
    print(compare_temperatures(20, 25))
    print(compare_temperatures(25, 25))