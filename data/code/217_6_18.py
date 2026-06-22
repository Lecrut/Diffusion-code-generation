def compare_numbers(a: str, b: str) -> bool:
    len_a = len(a)
    len_b = len(b)
    
    if len_a > len_b:
        return True
    elif len_a < len_b:
        return False
    
    for i in range(len_a):
        if a[i] > b[i]:
            return True
        elif a[i] < b[i]:
            return False
    
    return False

if __name__ == '__main__':
    num1 = "9876543210"
    num2 = "1234567890"
    
    result = compare_numbers(num1, num2)
    print(result)