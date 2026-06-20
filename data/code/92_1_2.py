def find_opposite_truth(truth):
    return not truth

if __name__ == '__main__':
    sample_values = {True: "True", False: "False"}
    for value in sample_values:
        result = find_opposite_truth(value)
        print(f"Opposite of {sample_values[value]} is {result}")