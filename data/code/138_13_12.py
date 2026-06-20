def evaluate_boolean_operations():
    truth_table = {(True, True): True, (True, False): False, (False, True): False, (False, False): False}

    def evaluate(a, b):
        return truth_table[a, b]
    result1 = evaluate(True, True)
    result2 = evaluate(True, False)
    result3 = evaluate(False, True)
    result4 = evaluate(False, False)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
if __name__ == '__main__':
    evaluate_boolean_operations()