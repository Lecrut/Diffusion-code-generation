def iterative_transform(data, repetitions, transformation):
    result = []
    for item in data:
        current_item = item
        for _ in range(repetitions):
            current_item = transformation(current_item)
        result.append(current_item)
    return result
def double(x):
    return x * 2
def add_one(x):
    return x + 1
if __name__ == '__main__':
    sample_data = [1, 5, 10]
    repetitions = 3
    transformed_data = iterative_transform(sample_data, repetitions, double)
    print(transformed_data)