if __name__ == '__main__':
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    grouped_dict = {k: [v] for k, v in zip(keys, values)}
    print(grouped_dict)