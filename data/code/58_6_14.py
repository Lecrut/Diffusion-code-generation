def access_first_element(data):
    return data[0]

def test_access_first_element():
    assert access_first_element([1, 2, 3]) == 1
    assert access_first_element(["a", "b", "c"]) == "a"
    assert access_first_element([True, False, True]) == True
    assert access_first_element([3.5, 2.5, 1.5]) == 3.5

if __name__ == '__main__':
    test_access_first_element()
    print("All tests passed.")