def print_first_and_last(strings):
    if not strings:
        raise ValueError("List must not be empty")
    print(strings[0])
    print(strings[-1])

if __name__ == '__main__':
    sample_list = ["alpha", "beta", "gamma", "delta"]
    print_first_and_last(sample_list)