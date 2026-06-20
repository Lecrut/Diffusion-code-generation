def check_first_and_last(data):
    if not data:
        raise ValueError("Input list is empty")
    return data[0], data[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(check_first_and_last(sample_list))
    
    try:
        sample_list_empty = []
        print(check_first_and_last(sample_list_empty))
    except ValueError as e:
        print(e)