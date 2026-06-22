def _validate_nonzero(first):
    if first == 0:
        raise ValueError("First argument must be non-zero for divisibility check")
    return True

def check_integer_properties(first, second, third):
    _validate_nonzero(first)
    pos_check = first > 0
    even_check = second % 2 == 0
    div_check = third % first == 0
    return (pos_check, even_check, div_check)

if __name__ == '__main__':
    sample_first = 5
    sample_second = 8
    sample_third = 15
    output = check_integer_properties(sample_first, sample_second, sample_third)
    print(output)