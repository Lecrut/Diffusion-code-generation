def get_divisors(n):
    if n == 0:
        return [0]
    
    divisors = []
    n_abs = abs(n)
    
    for i in range(1, int(n_abs**0.5) + 1):
        if n_abs % i == 0:
            divisors.append(i)
            if i != n_abs // i:
                divisors.append(n_abs // i)
    
    result = sorted(divisors)
    
    if n < 0:
        result = [-d for d in result]
        
    return result

if __name__ == '__main__':
    number = 28
    divisors = get_divisors(number)
    print(divisors)