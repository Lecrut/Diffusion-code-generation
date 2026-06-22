from operator import gt

def find_max(*args):
    if not args:
        raise ValueError("At least one argument is required")
    
    max_val = args[0]
    
    for val in args[1:]:
        if gt(val, max_val):
            max_val = val
            
    return max_val

if __name__ == '__main__':
    result = find_max(10, 45, 3, 89, 27)
    print(result)