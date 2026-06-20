def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    first_val, last_val = check_first_and_last(sample_list)
    print(f"First: {first_val}, Last: {last_val}")