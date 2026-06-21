def unique_items(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_items = ['pear', 'apple', 'kiwi', 'banana', 'apple', 'orange']
    print(unique_items(sample_items))