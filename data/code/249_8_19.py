def find_largest_item(tuples):
    if not all(isinstance(t, tuple) and len(t) > 1 for t in tuples):
        raise ValueError("All items must be tuples with at least two elements")
    
    return max(tuples, key=lambda x: x[1])

if __name__ == '__main__':
    sample_data = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
    print(find_largest_item(sample_data))