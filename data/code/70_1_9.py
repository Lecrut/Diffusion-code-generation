def check_first_and_last(data):
    if not data:
        raise ValueError("Input list is empty")
    return data[0], data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(f"First: {check_first_and_last(sample_list)[0]}, Last: {check_first_and_last(sample_list)[1]}")
    
    sample_list_two = [5]
    print(f"First: {check_first_and_last(sample_list_two)[0]}, Last: {check_first_and_last(sample_list_two)[1]}")
    
    try:
        sample_list_three = []
        print(check_first_and_last(sample_list_three))
    except ValueError as e:
        print(e)