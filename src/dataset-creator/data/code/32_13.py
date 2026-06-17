from collections import Counter
def count_elements(collection):
    return dict(Counter(collection))
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 2, 3, 6]
    result = count_elements(data)
    print(result)