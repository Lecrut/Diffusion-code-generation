from collections import Counter as StdCounter
def count_elements_optimized(collection):
    counts = {}
    for item in collection:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1
    return dict(counts)
if __name__ == '__main__':
    sample_data = [3, 'apple', 2.5, 'banana', 3, 'cherry', 2.5, 'apple']
    result = count_elements_optimized(sample_data)
    print(result)