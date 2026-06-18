def get_last_value(container):
    if not container:
        return None
    else:
        return container[-1]
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b')
    sample_string = "hello"
    empty_list = []
    print(get_last_value(sample_list))                  
    print(get_last_value(sample_tuple))                
    print(get_last_value(sample_string))               
    result_empty = get_last_value(empty_list)
    if result_empty is None:
        print("Empty container")