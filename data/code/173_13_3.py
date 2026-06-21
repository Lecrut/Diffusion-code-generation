def group_lists(keys, values):
    return {k: [v] for k, v in zip(keys, values)}

if __name__ == '__main__':
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    print(group_lists(keys, values))