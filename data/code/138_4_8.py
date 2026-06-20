def bitwise_operations(a, b):
    and_result = a and b
    or_result = a or b
    xor_result = a != b
    return [(a, b, and_result), (a, not b, or_result), (not a, b, xor_result), (not a, not b, xor_result)]

if __name__ == '__main__':
    table1 = bitwise_operations(True, True)
    table2 = bitwise_operations(True, False)
    table3 = bitwise_operations(False, True)
    table4 = bitwise_operations(False, False)
    print(table1)
    print(table2)
    print(table3)
    print(table4)