def deduplicate_and_sort(items):
    return sorted(set(items))
if __name__ == '__main__':
    data = ['banana', 'apple', 'cherry', 'date', 'elderberry']
    result = deduplicate_and_sort(data)
    print(result)