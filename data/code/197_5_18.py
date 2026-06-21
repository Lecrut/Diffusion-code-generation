ALLOWED_VALUES = frozenset([10, 20, 30, 40, 50])

def is_member(element):
    return element in ALLOWED_VALUES
if __name__ == '__main__':
    print(is_member(30))
    print(is_member(60))