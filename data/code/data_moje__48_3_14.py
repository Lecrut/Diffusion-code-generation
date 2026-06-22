def get_largest_value(d):
    return max(d.values())

if __name__ == '__main__':
    sample_data = {
        "a": 10,
        "b": 25,
        "c": 15,
        "d": 42
    }
    print(get_largest_value(sample_data))