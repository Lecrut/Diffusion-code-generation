def compare_two_simple_quantities_now_batch_process(samples):
    return [max(sample) - min(sample) for sample in samples]

if __name__ == '__main__':
    samples = [[3, 5, 1], [8, 2, 9], [4, 7, 6]]
    print(compare_two_simple_quantities_now_batch_process(samples))