def find_opposite_truth(value):
    return not value

if __name__ == '__main__':
    sample_values = [True, False]
    for val in sample_values:
        print(find_opposite_truth(val))