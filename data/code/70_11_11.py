def get_first_last(strings):
    if not strings:
        return None, None
    first = strings[0]
    last = strings[-1]
    return first, last

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    first, last = get_first_last(sample_list)
    print(f"First: {first}, Last: {last}")