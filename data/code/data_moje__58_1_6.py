def count_evens(a, b):
    if a > b:
        a, b = b, a
    
    start = a if a % 2 == 0 else a + 1
    end = b if b % 2 == 0 else b - 1
    
    if start > end:
        return 0
    
    return (end - start) // 2 + 1

if __name__ == '__main__':
    result = count_evens(10, 20)
    print(result)