def mean(collection):
    if not collection:
        raise ValueError("Collection cannot be empty")
    return sum(collection) / len(collection)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    try:
        average = mean(sample_values)
        print(average)
    except ValueError as e:
        print(e)