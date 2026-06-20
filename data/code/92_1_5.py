NOT_TRUE = False

def find_opposite_truth(truth):
    return NOT_TRUE if truth else True

if __name__ == '__main__':
    sample_values = [True, False]
    for value in sample_values:
        result = find_opposite_truth(value)
        print(f"Opposite of {value} is {result}")