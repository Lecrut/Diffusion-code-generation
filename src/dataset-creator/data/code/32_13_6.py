from collections import Counter
def count_elements_in_collection(collection):
    return dict(Counter(collection))
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 2, 3, 6]
    result = count_elements_in_collection(sample_data)
    print(result)