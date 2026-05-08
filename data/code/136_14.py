def check_conditions(condition_A, condition_B):
    result = []
    for a, b in zip(condition_A, condition_B):
        result.append(a and b)
    return result
if __name__ == '__main__':
    list_A = [True, False, True, True]
    list_B = [True, True, False, False]
    output = check_conditions(list_A, list_B)
    print(output)