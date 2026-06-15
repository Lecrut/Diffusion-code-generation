def iterative_transform(data, repetitions):
    result = []
    for item in data:
        current_item = item
        for _ in range(repetitions):
            current_item = item * 2 + 1
        result.append(current_item)
    return result
if __name__ == '__main__':
    sample_data = [1, 5, 10]
    repetitions = 3
    output = iterative_transform(sample_data, repetitions)
    print(output)