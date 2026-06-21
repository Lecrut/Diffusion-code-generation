MAX_KEY = lambda x: x

def find_maximum(iterable):
    return max(iterable, key=MAX_KEY)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    maximum_value = find_maximum(sample_list)
    print(maximum_value)