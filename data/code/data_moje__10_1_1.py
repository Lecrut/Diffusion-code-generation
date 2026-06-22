def get_first_element(lst):
    indices_map = {
        'first': 0
    }
    return lst[indices_map['first']]

if __name__ == '__main__':
    data = ['alpha', 'beta', 'gamma']
    result = get_first_element(data)
    print(result)