def km_to_miles(km):
    return km * 0.621371

def test_km_to_miles():
    assert abs(km_to_miles(0) - 0) < 1e-9, "Test case 1 failed"
    assert abs(km_to_miles(1) - 0.621371) < 1e-9, "Test case 2 failed"
    assert abs(km_to_miles(10) - 6.21371) < 1e-9, "Test case 3 failed"
    assert abs(km_to_miles(100) - 62.1371) < 1e-9, "Test case 4 failed"

if __name__ == '__main__':
    test_km_to_miles()