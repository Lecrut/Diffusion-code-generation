def group_pairs(keys, values):
    return {k: [v] for k, v in zip(keys, values)}

if __name__ == '__main__':
    keys = ['x', 'y', 'z']
    values = [10, 20, 30]
    grouped_dict = group_pairs(keys, values)
    print(grouped_dict)