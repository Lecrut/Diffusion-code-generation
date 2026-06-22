def safe_last_element(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    try:
        return lst[-1]
    except IndexError:
        raise ValueError('List is empty')
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = ['a', 'b', 'c']
    sample_list_3 = []
    try:
        print(safe_last_element(sample_list_1))
    except Exception as e:
        print(e)
    try:
        print(safe_last_element(sample_list_2))
    except Exception as e:
        print(e)
    try:
        print(safe_last_element(sample_list_3))
    except Exception as e:
        print(e)