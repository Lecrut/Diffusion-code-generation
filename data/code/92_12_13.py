def opposite_boolean(boolean_str):
    return 'True' if boolean_str.lower() == 'false' else 'False'
if __name__ == '__main__':
    print(opposite_boolean('True'))
    print(opposite_boolean('FALSE'))
    print(opposite_boolean('true'))
    print(opposite_boolean('false'))