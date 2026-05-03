def compare_temperatures(temp1, temp2):
    if temp1 > temp2:
        return "greater"
    elif temp1 < temp2:
        return "less"
    else:
        return "equal"
def test_compare_temperatures():
    assert compare_temperatures(30, 20) == "greater"
    assert compare_temperatures(15, 30) == "less"
    assert compare_temperatures(25, 25) == "equal"
    assert compare_temperatures(100, 50) == "greater"
    assert compare_temperatures(5, 10) == "less"
if __name__ == '__main__':
    test_compare_temperatures()