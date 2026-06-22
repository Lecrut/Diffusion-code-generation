def km_to_miles(km):
    return km * 0.621371

def test_km_to_miles():
    assert abs(km_to_miles(0) - 0) < 1e-9, "Test case 1 failed"
    assert abs(km_to_miles(1) - 0.621371) < 1e-9, "Test case 2 failed"
    assert abs(km_to_miles(10) - 6.21371) < 1e-9, "Test case 3 failed"
    print("All test cases passed")

if __name__ == '__main__':
    print(f"0 km is {km_to_miles(0)} miles")
    print(f"1 km is {km_to_miles(1)} miles")
    print(f"10 km is {km_to_miles(10)} miles")
    test_km_to_miles()