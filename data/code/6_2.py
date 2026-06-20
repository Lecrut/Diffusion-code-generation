def weight_difference_generator(pairs):
    for pair in pairs:
        if len(pair) >= 2:
            yield abs(pair[0] - pair[1])

if __name__ == '__main__':
    sample_data = [(10, 15), (20, 5), (8, 8), (100, 120)]
    result = list(weight_difference_generator(sample_data))
    print(result)