condition_dict = {
    'a': True,
    'b': False
}

def check_conditions(a_key, b_key):
    return condition_dict[a_key] and condition_dict[b_key]

if __name__ == '__main__':
    result = check_conditions('a', 'b')
    print(result)