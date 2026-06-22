def validate_collection(collection):
    if not isinstance(collection, (list, tuple, set)):
        raise ValueError("Input must be a list, tuple, or set")
    if not all(isinstance(x, (int, float)) for x in collection):
        raise ValueError("All elements must be numbers")

def calculate_mean(collection):
    validate_collection(collection)
    return sum(collection) / len(collection)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_mean(sample_values))