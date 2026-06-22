sample_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5
}

def reverse_dict_print(d):
    keys = list(d.keys())
    keys.reverse()
    for key in keys:
        print(f"{key}: {d[key]}")

if __name__ == '__main__':
    reverse_dict_print(sample_dict)