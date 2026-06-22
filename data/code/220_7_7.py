def mean_of_collection(collection):
    return sum(collection) / len(collection)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(mean_of_collection(sample_values))