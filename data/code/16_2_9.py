def get_head(t):
    return t[0]

if __name__ == '__main__':
    print(get_head((1, 2, 3)))
    print(get_head(('a', 'b', 'c')))
    print(get_head((True, False)))