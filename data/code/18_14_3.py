def run_length_encoding(data):
    if not data:
        return
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            yield (count, data[i - 1])
            count = 1
    yield (count, data[-1])

if __name__ == '__main__':
    sample_input = "aaabbccccddee"
    result = list(run_length_encoding(sample_input))
    print(result)