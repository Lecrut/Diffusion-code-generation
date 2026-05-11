def group_tuples(data):
    result = {}
    for item, category in data:
        if category not in result:
            result[category] = []
        result[category].append(item)
    return result
if __name__ == '__main__':
    sample_data = [
        ('apple', 'fruit'),
        ('carrot', 'vegetable'),
        ('banana', 'fruit'),
        ('broccoli', 'vegetable'),
        ('orange', 'fruit'),
        ('spinach', 'vegetable')
    ]
    grouped_data = group_tuples(sample_data)
    print(grouped_data)