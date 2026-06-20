def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last

if __name__ == '__main__':
    sample_list = [42, 84, 126, 168, 210]
    result_first, result_last = check_first_and_last(sample_list)
    print(f"First: {result_first}, Last: {result_last}")