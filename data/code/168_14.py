def group_tuples(data):
    result = {}
    for item, category in data:
        if category not in result:
            result[category] = []
        result[category].append(item)
    return result
if __name__ == '__main__':
    data = [('apple', 'fruit'), ('carrot', 'vegetable'), ('banana', 'fruit'), ('broccoli', 'vegetable'), ('lettuce', 'vegetable')]
    grouped_data = group_tuples(data)
    print(grouped_data)