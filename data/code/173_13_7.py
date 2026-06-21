KEYS = ['a', 'b', 'c']
VALUES = [1, 2, 3]

def group_lists(keys, values):
    return {k: [v] for k, v in zip(keys, values)}

if __name__ == '__main__':
    grouped_dict = group_lists(KEYS, VALUES)
    print(grouped_dict)