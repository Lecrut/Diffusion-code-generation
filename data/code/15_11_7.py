def get_penultimate_value(items):
    if len(items) < 2:
        raise ValueError("List must contain at least two elements")
    return items[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        result = get_penultimate_value(sample_list)
        print(result)
    except ValueError as e:
        print(e)
    
    empty_list = []
    try:
        get_penultimate_value(empty_list)
    except ValueError as e:
        print(e)
    
    short_list = [1]
    try:
        get_penultimate_value(short_list)
    except ValueError as e:
        print(e)