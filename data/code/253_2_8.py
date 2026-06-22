def find_the_middle_value_among_three_batch_process(values):
    return sorted(values)[1]

if __name__ == '__main__':
    sample_values = [3, 1, 2]
    print(find_the_middle_value_among_three_batch_process(sample_values))