def find_opposite_truth(flag):
    if flag is True:
        result = False
    else:
        result = True
    return result

if __name__ == '__main__':
    test_input = False
    output = find_opposite_truth(test_input)
    print(output)
    test_input = True
    output = find_opposite_truth(test_input)
    print(output)