def print_first_last(strings):
    if strings:
        print(strings[0])
        print(strings[-1])

if __name__ == '__main__':
    sample = ["apple", "banana", "cherry"]
    print_first_last(sample)