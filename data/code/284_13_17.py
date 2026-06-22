def reverse_dict_by_key(d):
    keys = list(d.keys())
    keys.sort(reverse=True)
    for key in keys:
        print(f"{key}: {d[key]}")

if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    reverse_dict_by_key(sample_dict)