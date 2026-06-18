import sys
def remove_duplicates(iterable):
    seen = set()
    result = []
    for item in iterable:
        if id(item) not in seen:
            if item not in seen:
                seen.add(item)
                result.append(item)
    return result
if __name__ == '__main__':
    data = [1, 2, 'a', 'b', (3, 4), (5, 6), 1, 'c', 'd'] 
    unique_data = remove_duplicates(data)
    print(unique_data)