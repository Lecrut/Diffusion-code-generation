def get_penultimate_value(data):
    if len(data) < 2:
        raise ValueError("List must contain at least two elements")
    return data[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_penultimate_value(sample_list))
    print(get_penultimate_value([1, 2]))
    print(get_penultimate_value(['a', 'b', 'c']))