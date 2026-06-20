def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    result = check_first_and_last(sample_list)
    print(f"First: {result[0]}, Last: {result[1]}")