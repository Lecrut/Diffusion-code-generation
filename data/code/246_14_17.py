sum_dict = {'a': 5, 'b': 3}

def calculate_sum(dictionary):
    return dictionary['a'] + dictionary['b']

if __name__ == '__main__':
    result = calculate_sum(sum_dict)
    print(result)