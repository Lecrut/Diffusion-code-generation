def count_even_numbers(a, b):
    if a > b:
        a, b = b, a
    
    start = a if a % 2 == 0 else a + 1
    end = b if b % 2 == 0 else b - 1
    
    if start > end:
        return 0
    
    count = (end - start) // 2 + 1
    return count

if __name__ == '__main__':
    a = 2
    b = 10
    result = count_even_numbers(a, b)
    print(result)