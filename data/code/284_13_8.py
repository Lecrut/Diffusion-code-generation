def reverse_dict_print(d):
    for key in sorted(d.keys(), reverse=True):
        print(key, d[key])

if __name__ == '__main__':
    sample_dict = {'apple': 3, 'banana': 2, 'cherry': 5}
    reverse_dict_print(sample_dict)