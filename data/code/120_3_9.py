def are_values_equal(val1, val2):
    return val1 == val2
if __name__ == '__main__':
    result1 = are_values_equal(7, 7)
    result2 = are_values_equal('world', 'world')
    result3 = are_values_equal(True, True)
    print(result1)
    print(result2)
    print(result3)