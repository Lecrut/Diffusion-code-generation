def find_largest_item(tuples):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in tuples):
        raise ValueError("All items must be tuples with exactly two elements")
    
    return max(tuples, key=lambda x: x[1])

if __name__ == '__main__':
    sample_tuples = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
    print(find_largest_item(sample_tuples))