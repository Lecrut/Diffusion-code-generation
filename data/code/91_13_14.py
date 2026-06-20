TRUE = True
FALSE = False

def negate_boolean(b):
    return b ^ TRUE

if __name__ == '__main__':
    print(negate_boolean(TRUE))
    print(negate_boolean(FALSE))