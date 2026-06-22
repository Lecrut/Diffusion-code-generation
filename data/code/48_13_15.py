def find_largest_integer():
    scores = (92, 85, 'N/A', 78, 95, 'missing', 88, 72, 91, 'error', 89)
    valid_integers = [score for score in scores if isinstance(score, int) and not isinstance(score, bool)]
    
    if not valid_integers:
        return None
    
    max_val = valid_integers[0]
    for val in valid_integers[1:]:
        if val > max_val:
            max_val = val
            
    return max_val

if __name__ == '__main__':
    result = find_largest_integer()
    print(result)