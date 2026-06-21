def get_penultimate_item(items):
    if len(items) < 2:
        raise ValueError("List must contain at least two elements")
    return items[-2]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = ['a', 'b']
    sample_list_3 = [1]
    
    print(get_penultimate_item(sample_list_1))
    print(get_penultimate_item(sample_list_2))
    try:
        print(get_penultimate_item(sample_list_3))
    except ValueError as e:
        print(str(e))