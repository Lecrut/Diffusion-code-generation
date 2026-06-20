def check_number(num):
    conditions = {
        'positive': num > 0,
        'even': num % 2 == 0,
        'less_than_100': num < 100
    }
    
    if all(conditions.values()):
        return f"{num} is positive, even, and less than 100."
    elif conditions['positive'] and conditions['even']:
        return f"{num} is positive and even, but not less than 100."
    elif conditions['positive'] and conditions['less_than_100']:
        return f"{num} is positive and less than 100, but not even."
    elif conditions['even'] and conditions['less_than_100']:
        return f"{num} is even and less than 100, but not positive."
    elif conditions['positive']:
        return f"{num} is positive, but not even or less than 100."
    elif conditions['even']:
        return f"{num} is even, but not positive or less than 100."
    elif conditions['less_than_100']:
        return f"{num} is less than 100, but not positive or even."
    else:
        return f"{num} does not meet any of the specified conditions."

if __name__ == '__main__':
    print(check_number(2))
    print(check_number(4))
    print(check_number(98))
    print(check_number(102))