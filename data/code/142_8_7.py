def compare_booleans():
    bool_map = {True: 'Equal', False: 'Not Equal'}
    return bool_map[True == False]

if __name__ == '__main__':
    result = compare_booleans()
    print(result)