def find_factors(n):
    if n < 1:
        return []
    if n == 1:
        return [1]
    
    found_divisors = [1]
    upper_bound = int(n**0.5)
    
    for candidate in range(2, upper_bound + 1):
        if n % candidate == 0:
            found_divisors.append(candidate)
            complement = n // candidate
            if complement != candidate:
                found_divisors.append(complement)
    
    found_divisors.sort()
    return found_divisors

if __name__ == '__main__':
    target_number = 7919
    factors_list = find_factors(target_number)
    print(factors_list)