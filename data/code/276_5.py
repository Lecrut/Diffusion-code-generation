def iterative_transform(data, repetitions, transform_func):
    result = []
    for item in data:
        current_item = item
        for _ in range(repetitions):
            current_item = transform_func(current_item)
        result.append(current_item)
    return result
def double(x):
    return x * 2
if __name__ == '__main__':
    sample_data = [1, 5, 10]
    repetitions = 3
    processed_data = iterative_transform(sample_data, repetitions, double)
    print(processed_data)