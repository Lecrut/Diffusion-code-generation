def tuple_exists_in_list(tuple_to_check, list_of_tuples):
    if not isinstance(tuple_to_check, tuple) or not all((isinstance(item, tuple) for item in list_of_tuples)):
        raise ValueError('tuple_to_check must be a tuple and list_of_tuples must be a list of tuples')
    return tuple_to_check in list_of_tuples
if __name__ == '__main__':
    sample_tuple = ('orange', 'grape')
    sample_list = [('apple', 'banana'), ('cherry', 'date'), ('orange', 'grape')]
    result = tuple_exists_in_list(sample_tuple, sample_list)
    print(result)