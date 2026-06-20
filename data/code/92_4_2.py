def opposite_boolean(boolean_str):
    return 'True' if boolean_str == 'False' else 'False'
if __name__ == '__main__':
    print(opposite_boolean('True'))
    print(opposite_boolean('False'))