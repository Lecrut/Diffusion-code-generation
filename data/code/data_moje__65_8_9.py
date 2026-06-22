def feet_to_inches(feet):
    return feet * 12

def test_feet_to_inches():
    assert feet_to_inches(12) == 144

if __name__ == '__main__':
    test_feet_to_inches()
    result = feet_to_inches(12)
    print(result)