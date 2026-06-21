def group_by_key(keys, values):
    return {k: [v] for k, v in zip(keys, values)}

if __name__ == '__main__':
    keys = ['apple', 'banana', 'cherry']
    values = [1, 2, 3]
    print(group_by_key(keys, values))