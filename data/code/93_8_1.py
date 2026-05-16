if __name__ == '__main__':
    a = False
    b = False
    if a and b:
        print('Both are true')
    elif a and not b:
        print('Only a is true')
    elif not a and b:
        print('Only b is true')
    else:
        print('Both are false')