def repeat_and_merge_dict(d, V):
    result = {}
    for _ in range(V):
        for key, value in d.items():
            if isinstance(value, dict):
                if key not in result:
                    result[key] = {}
                repeat_and_merge_dict(value, V)
            else:
                if key not in result:
                    result[key] = []
                result[key].append(value)
    return result

if __name__ == '__main__':
    sample_dict = {
        'a': 1,
        'b': {'c': 2, 'd': {'e': 3}},
        'f': [4, 5]
    }
    V = 2
    print(repeat_and_merge_dict(sample_dict, V))