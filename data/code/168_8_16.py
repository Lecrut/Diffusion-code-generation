def group_by_string_length(items):
    GROUP_SIZES = {
        'small': 10,
        'medium': 20,
        'large': 30
    }

    def get_group_size(item):
        return len(str(item))

    groups = {
        size: [] for size in GROUP_SIZES.values()
    }

    for item in items:
        group_size = get_group_size(item)
        if group_size <= GROUP_SIZES['small']:
            groups[GROUP_SIZES['small']].append(item)
        elif group_size <= GROUP_SIZES['medium']:
            groups[GROUP_SIZES['medium']].append(item)
        else:
            groups[GROUP_SIZES['large']].append(item)

    return groups

if __name__ == '__main__':
    sample_items = [
        1, 234567890, 'hello', 'world', 'python', 'programming',
        [1, 2], ['a', 'b', 'c'], {'key': 'value'}
    ]
    result = group_by_string_length(sample_items)
    print(result)