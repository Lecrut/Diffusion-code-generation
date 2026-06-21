def check_first_and_last(data):
    if not data:
        return None, None
    first = data[0]
    last = data[-1]
    return first, last

if __name__ == '__main__':
    sample_values = {
        'list1': [10, 20, 30, 40, 50],
        'list2': [5],
        'list3': [],
        'list4': [99]
    }
    
    for key, value in sample_values.items():
        first_val, last_val = check_first_and_last(value)
        print(f"List: {key}, First: {first_val}, Last: {last_val}")