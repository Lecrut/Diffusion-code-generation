def get_last(collection):
    return collection[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (100, 200, 300)
    sample_string = "hello"
    
    print(get_last(sample_list))
    print(get_last(sample_tuple))
    print(get_last(sample_string))