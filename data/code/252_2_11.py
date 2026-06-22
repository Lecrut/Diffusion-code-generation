def compare_two_simple_quantities_now_batch_process(sample_values):
    return [x * 2 for x in sample_values]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(compare_two_simple_quantities_now_batch_process(sample_values))