def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28, 35]
    result = check_first_and_last(sample_list)
    print(f"First: {result[0]}, Last: {result[1]}")
    
    sample_list_single = [9]
    result_single = check_first_and_last(sample_list_single)
    print(f"First: {result_single[0]}, Last: {result_single[1]}")