def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(f"First: {check_first_and_last(sample_list)[0]}, Last: {check_first_and_last(sample_list)[1]}")
    sample_list_two = [5]
    print(f"First: {check_first_and_last(sample_list_two)[0]}, Last: {check_first_and_last(sample_list_two)[1]}")
    sample_list_three = []
    print(f"First: {check_first_and_last(sample_list_three)[0]}, Last: {check_first_and_last(sample_list_three)[1]}")
    sample_list_four = [99]
    print(f"First: {check_first_and_last(sample_list_four)[0]}, Last: {check_first_and_last(sample_list_four)[1]}")