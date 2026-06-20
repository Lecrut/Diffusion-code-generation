def evaluate_logic(a, b):
    return a & b

if __name__ == '__main__':
    sample_values = {True: True, False: False}
    result = evaluate_logic(sample_values[True], sample_values[False])
    print(result)