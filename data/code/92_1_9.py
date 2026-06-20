def find_opposite_truth(truth):
    return not truth

if __name__ == '__main__':
    samples = {True: "True", False: "False"}
    for value in samples:
        result = find_opposite_truth(value)
        print(f"Opposite of {samples[value]} is {result}")