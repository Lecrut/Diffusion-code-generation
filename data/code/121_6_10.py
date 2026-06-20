def compare_tuples(t1, t2):
    if not (isinstance(t1, tuple) and isinstance(t2, tuple)):
        raise ValueError("Both arguments must be tuples")
    
    for a, b in zip(t1, t2):
        if a > b:
            return t1
        elif a < b:
            return t2
    
    return t1 if len(t1) >= len(t2) else t2

if __name__ == '__main__':
    print(compare_tuples((3, 4), (2, 5)))
    print(compare_tuples(('apple', 'banana'), ('banana', 'cherry')))