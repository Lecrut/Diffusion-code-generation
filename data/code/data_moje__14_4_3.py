def get_third_item(items):
    if not isinstance(items, list):
        raise TypeError('Input must be a list.')
    if not all((isinstance(item, str) for item in items)):
        raise TypeError('All items in the list must be strings.')
    if len(items) < 3:
        raise IndexError('List must have at least three items.')
    return items[2]
if __name__ == '__main__':
    sample_list = ['first', 'second', 'third', 'fourth']
    result = get_third_item(sample_list)
    print(result)