def opposite_bool_str(s):
    if s == 'True':
        return 'False'
    elif s == 'False':
        return 'True'
    else:
        raise ValueError(f"Unsupported boolean string: {s}")

if __name__ == '__main__':
    print(opposite_bool_str('True'))
    print(opposite_bool_str('False'))
    print(opposite_bool_str('True'))