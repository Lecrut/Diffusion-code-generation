import json
def reverse_sequence(item):
    if not isinstance(item, (list, tuple)):
        return item
    reversed_list = []
    for sub_item in item:
        result = reverse_sequence(sub_item)
        reversed_list.append(result)
    if isinstance(item, list):
        return reversed(reversed_list[::-1])
    else:
        return reversed_list
if __name__ == '__main__':
    sample_data = [
        1,
        "hello",
        {
            'a': [[2, 3], {'b': ['x', 'y']}],
            None: []
        },
        (4, 5),
        [],
        ("nested", ["tuple"], {"deep": [True]})
    ]
    try:
        result = reverse_sequence(sample_data)
        print(json.dumps(result, default=str))
    except Exception as e:
        print(f"Error occurred: {e}")