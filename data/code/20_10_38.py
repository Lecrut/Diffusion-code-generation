def are_objects_equal(x, y):
    return x == y

if __name__ == '__main__':
    LIST1 = [1, 2, 3]
    LIST2 = [1, 2, 3]
    TUPLE1 = (1, 2, 3)
    STRING1 = 'hello'
    STRING2 = 'hello'
    
    print(are_objects_equal(LIST1, LIST2))
    print(are_objects_equal(LIST1, TUPLE1))
    print(are_objects_equal(STRING1, STRING2))