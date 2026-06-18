def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if id(item) not in seen and (item not in result):
            seen.add(id(item))
            result.append(item)
    return result
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]