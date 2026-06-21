UNIQUE_SET = set()

def unique_items(items):
    seen = UNIQUE_SET.copy()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    print(unique_items(sample_items))