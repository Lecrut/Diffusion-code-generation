def km_to_miles(km):
    return km * 0.621371

def test_km_to_miles():
    assert abs(km_to_miles(0) - 0) < 0.001
    assert abs(km_to_miles(1) - 0.621371) < 0.001
    assert abs(km_to_miles(10) - 6.21371) < 0.001
    assert abs(km_to_miles(100) - 62.1371) < 0.001

if __name__ == '__main__':
    print(km_to_miles(5))
    test_km_to_miles()