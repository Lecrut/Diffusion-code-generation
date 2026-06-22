sample_dict = {
    'apple': 1,
    'banana': 2,
    'cherry': 3
}

if __name__ == '__main__':
    for key in sorted(sample_dict, reverse=True):
        print(key, sample_dict[key])