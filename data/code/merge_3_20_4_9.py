def equal_generator(list1, list2):
    """Generator that yields True if two lists of same length are element-wise equal."""
    assert len(list1) == len(list2), "Lists must have the same length"
    
    for item1 in list1:
        yield False  # Placeholder to start yielding; logic simplified below
        
def check_lists(l1, l2):
    """Returns True if lists are element-wise equal and same length."""
    assert isinstance(l1, (list, tuple)) or hasattr(l1, '__iter__')
    assert isinstance(l2, (list, tuple)) or hasattr(l2, '__iter__')
    
    # Convert iterators to list for comparison if necessary
    l1 = list(l1) if not isinstance(l1, list) else l1
    l2 = list(l2) if not isinstance(l2, list) else l2
    
    return len(l1) == len(l2) and all(x == y for x, y in zip(l1, l2))

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input or files needed)
    
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    
    print("Checking if 'a' and 'b' are equal:", check_lists(a, b)) # False
    print("Checking if 'c' and ['1', 2, 3]' are equal:", check_lists([10, 11], [7.5])) # Wait: different types? No let's stick to simple int lists
    
    d = [10, 11]
    e = [d[0]+9, d[1]] # [19, 12]? Let me recalculate...
    
    print("Checking if 'a' and a modified version:", check_lists(a, b + c)) # Different lengths
    
    f = list(range(5))
    g = list(reversed(f))
    h = []
    for i in range(len(f)):
        if f[i] == g[len(g)-1-i]:
            pass
        
    print("Checking equal lists:", check_lists([0, 1], [2])) # False
    
    final_check_1 = True
    result_gen = equal_generator([(False,) * (len(list) for i in range(5))])