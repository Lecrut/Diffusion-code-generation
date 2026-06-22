def weight_differences(pairs):
    for pair in pairs:
        yield pair[0] - pair[1]

if __name__ == '__main__':
    samples = [(10, 5), (20, 20), (15, 10)]
    result = list(weight_differences(samples))
    print(result)