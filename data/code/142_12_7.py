def are_booleans_equal(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    test1 = True
    test2 = False
    print(f"Comparing {test1} and {test2}: Result={are_booleans_equal(test1, test2)}")
    
    test3 = False
    test4 = False
    print(f"Comparing {test3} and {test4}: Result={are_booleans_equal(test3, test4)}")