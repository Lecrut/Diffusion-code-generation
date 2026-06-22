def compare_two_simple_quantities_now_batch_process(sample_values):
    return [max(a, b) for a, b in sample_values]

if __name__ == '__main__':
    sample_values = [(3, 5), (10, 2), (7, 7)]
    print(compare_two_simple_quantities_now_batch_process(sample_values))