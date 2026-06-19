def access_first_element(data):
    return data[0]

if __name__ == '__main__':
    sample_integers = [42, 84, 168]
    sample_strings = ["hello", "world", "test"]
    sample_floats = [3.14159, 2.71828, 1.41421]
    sample_booleans = [True, False, True]

    assert access_first_element(sample_integers) == 42
    print(f"First element of integers: {access_first_element(sample_integers)}")

    assert access_first_element(sample_strings) == "hello"
    print(f"First element of strings: {access_first_element(sample_strings)}")

    assert access_first_element(sample_floats) == 3.14159
    print(f"First element of floats: {access_first_element(sample_floats)}")

    assert access_first_element(sample_booleans) == True
    print(f"First element of booleans: {access_first_element(sample_booleans)}")