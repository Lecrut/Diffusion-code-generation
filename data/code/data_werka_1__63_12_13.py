def get_first_item(iterable):
    if not iterable:
        return None
    return next(iter(iterable))

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    print(get_first_item(sample_list))
    
    sample_tuple = (40, 50)
    print(get_first_item(sample_tuple))
    
    sample_string = "hello"
    print(get_first_item(sample_string))
    
    empty_list = []
    print(get_first_item(empty_list))
    
    empty_tuple = ()
    print(get_first_item(empty_tuple))
    
    empty_string = ""
    print(get_first_item(empty_string))