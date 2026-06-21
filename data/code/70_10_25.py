def print_first_and_last(strings):
    if not strings:
        raise ValueError("List must contain at least one element")
    print(strings[0])
    print(strings[-1])

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    print_first_and_last(sample_list)