def compare_large_integers(a, b):
    if not all(isinstance(x, int) and isinstance(y, int) for x in a for y in b):
        raise ValueError("Both inputs must be lists of integers.")
    
    size_a = len(a)
    size_b = len(b)
    
    if size_a > size_b:
        return (a, "greater")
    elif size_b > size_a:
        return (b, "greater")
    else:
        sum_a = sum(a)
        sum_b = sum(b)
        
        if sum_a > sum_b:
            return (a, "greater")
        elif sum_b > sum_a:
            return (b, "greater")
        else:
            return (a, "equal")

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7, 8]
    list4 = [9]
    
    result1 = compare_large_integers(list1, list2)
    print(result1)
    result2 = compare_large_integers(list3, list4)
    print(result2)