def count_evens(start, end):
    count = 0
    current = start
    limit = end
    if start > limit:
        return 0
    
    if start % 2 == 0:
        start_val = start
    else:
        start_val = start + 1
    
    if start_val > limit:
        return 0
    
    end_val = limit
    if limit % 2 != 0:
        end_val = limit - 1
    
    if start_val > end_val:
        return 0
    
    count = ((end_val - start_val) >> 1) + 1
    return count

if __name__ == '__main__':
    start = 10
    end = 20
    result = count_evens(start, end)
    print(result)