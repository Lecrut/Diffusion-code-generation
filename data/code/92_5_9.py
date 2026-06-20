def opposite_truth(value):
    return not value

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    for value in sample_values:
        print(opposite_truth(value))