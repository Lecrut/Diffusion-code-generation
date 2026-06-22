def mean(collection):
    if not collection:
        return 0
    return sum(collection) / len(collection)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(mean(sample_values))