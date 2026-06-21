def unique_items(items):
    seen = set()
    result = []
    for item in items:
        if not isinstance(item, str):
            raise ValueError("All items must be strings")
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    print(unique_items(sample_items))