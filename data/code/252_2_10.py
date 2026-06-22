def compare_two_simple_quantities_now_batch_process(samples):
    return [max(sample) - min(sample) for sample in samples]

if __name__ == '__main__':
    samples = [[3, 5, 1], [2, 8, 4], [7, 6, 9]]
    print(compare_two_simple_quantities_now_batch_process(samples))