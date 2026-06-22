def count_even(start, end):
    if start > end:
        start, end = end, start
    
    start_even = start if start % 2 == 0 else start + 1
    end_even = end if end % 2 == 0 else end - 1
    
    if start_even > end_even:
        return 0
    
    return (end_even - start_even) // 2 + 1

if __name__ == '__main__':
    result = count_even(1, 10)
    print(result)
    result2 = count_even(4, 4)
    print(result2)
    result3 = count_even(-5, 5)
    print(result3)