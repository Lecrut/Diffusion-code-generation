def find_largest_item(tuples):
    if not all(isinstance(t, tuple) and len(t) == 2 for t in tuples):
        raise ValueError("All items must be tuples with exactly two elements")
    
    return max(tuples, key=lambda x: x[1])

if __name__ == '__main__':
    sample_tuples = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
    print(find_largest_item(sample_tuples))