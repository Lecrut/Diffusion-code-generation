def last_element(collection):
    return collection[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = (10, 20, 30)
    sample_string = "hello"
    print(last_element(sample_list))
    print(last_element(sample_tuple))
    print(last_element(sample_string))