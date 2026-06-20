def find_opposite_truth(truth):
    return not truth

if __name__ == '__main__':
    test_cases = {True: "True", False: "False"}
    for value, description in test_cases.items():
        result = find_opposite_truth(value)
        print(f"Opposite of {description} is {result}")