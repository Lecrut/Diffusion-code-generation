def compare_byte_sizes(a, b):
    if len(a) > len(b):
        return a
    elif len(b) > len(a):
        return b
    else:
        return a

if __name__ == '__main__':
    obj1 = b'hello'
    obj2 = b'world'
    print(compare_byte_sizes(obj1, obj2))

    obj3 = b'abcde'
    obj4 = b'fghij'
    print(compare_byte_sizes(obj3, obj4))

    obj5 = b''
    obj6 = b'a'
    print(compare_byte_sizes(obj5, obj6))