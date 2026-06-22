sample_dict = {
    'apple': 1,
    'banana': 2,
    'cherry': 3
}

def print_reverse_dict(dictionary):
    for key in sorted(dictionary, reverse=True):
        print(f"{key}: {dictionary[key]}")

if __name__ == '__main__':
    print_reverse_dict(sample_dict)