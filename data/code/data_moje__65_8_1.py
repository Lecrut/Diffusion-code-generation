def feet_to_inches(feet):
    return feet * 12

if __name__ == '__main__':
    result = feet_to_inches(12)
    assert result == 144
    print(result)