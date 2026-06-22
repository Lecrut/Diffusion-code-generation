def reverse_dict_print(d):
    for key in sorted(d.keys(), reverse=True):
        print(f"{key}: {d[key]}")

if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    reverse_dict_print(sample_dict)