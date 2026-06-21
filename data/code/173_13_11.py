KEYS = ['x', 'y', 'z']
VALUES = [10, 20, 30]

def group_lists(keys=KEYS, values=VALUES):
    return {k: v for k, v in zip(keys, values)}

if __name__ == '__main__':
    result = group_lists()
    print(result)