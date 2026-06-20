def are_values_equal(val1, val2):
    return val1 == val2
if __name__ == '__main__':
    result1 = are_values_equal(7, 7)
    print(result1)
    result2 = are_values_equal('apple', 'banana')
    print(result2)
    result3 = are_values_equal(0.5, 0.5)
    print(result3)