def check_number(n):
    is_positive = n > 0
    is_even = n % 2 == 0
    is_less_than_100 = n < 100
    
    if is_positive and is_even and is_less_than_100:
        return f"{n} is positive, even, and less than 100."
    elif not is_positive:
        return f"{n} is not positive."
    elif not is_even:
        return f"{n} is positive but odd."
    elif not is_less_than_100:
        return f"{n} is positive and even but not less than 100."
    else:
        return f"{n} does not meet the criteria."

if __name__ == '__main__':
    print(check_number(50))
    print(check_number(-10))
    print(check_number(101))
    print(check_number(51))