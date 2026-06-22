MAX_DEPTH = 100

def count_items(nested_list, depth=0):
    if depth >= MAX_DEPTH:
        raise RecursionError("Maximum recursion depth exceeded")
    
    total_count = 0
    for item in nested_list:
        if isinstance(item, list):
            total_count += count_items(item, depth + 1)
        else:
            total_count += 1
    return total_count

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    print(count_items(sample_list))