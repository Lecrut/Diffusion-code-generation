def find_largest_robust(lists):
    if not lists:
        return None
    largest = -float('inf')
    for lst in lists:
        if not lst:
            continue
        current_max = max(lst)
        if current_max > largest:
            largest = current_max
    return largest
if __name__ == '__main__':
    test_cases = [
        ([ -10, -5, -20 ], [ 1, 5, 10 ]),                 
        ([ 0, -1, -5 ], [ -100, -50, -10 ]),               
        ([ 500, 600, 700 ], [ 10, 20, 30 ]),                  
        ([-10, -5], [ -1, -5, -10 ]),                      
        ([ 0 ], [ -1, 0, 5 ]),                             
        ([], [ 1, 2, 3 ])                                  
    ]
    for lists in test_cases:
        result = find_largest_robust(lists)
        print(f"Input Lists: {lists}")
        print(f"Result: {result}\n")