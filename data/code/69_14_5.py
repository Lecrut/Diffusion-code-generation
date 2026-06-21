def get_elements(lst):
    if not lst:
        return ()
    
    first = lst[0]
    last = lst[-1]
    middle = lst[len(lst) // 2] if len(lst) % 2 != 0 else None
    
    return (first, last, middle)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_elements(sample_list)
    print(result)