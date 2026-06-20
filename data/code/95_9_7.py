def combine_checks(is_positive, is_even, is_less_than_100):
    if is_positive and is_even and is_less_than_100:
        return "Number is positive, even, and less than 100."
    elif is_positive and is_even:
        return "Number is positive and even."
    elif is_positive and is_less_than_100:
        return "Number is positive and less than 100."
    elif is_even and is_less_than_100:
        return "Number is even and less than 100."
    elif is_positive:
        return "Number is positive."
    elif is_even:
        return "Number is even."
    elif is_less_than_100:
        return "Number is less than 100."
    else:
        return "Number does not meet any criteria."

if __name__ == '__main__':
    sample_values = [
        (True, True, True),
        (False, False, False),
        (True, False, True),
        (False, True, False),
        (True, True, False)
    ]
    
    for values in sample_values:
        result = combine_checks(*values)
        print(result)