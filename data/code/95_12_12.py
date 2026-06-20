def validate_input(n):
    if n > 0 and n % 2 == 0 and n < 100:
        return True
    else:
        return False

def combine_and_report(a, b, c):
    results = {}
    for val in [a, b, c]:
        name = 'a' if val == a else 'b' if val == b else 'c'
        if validate_input(val):
            results[name] = 'Pass'
        else:
            results[name] = 'Fail'
    return results

if __name__ == '__main__':
    sample_values = (50, 20, 98)
    result = combine_and_report(*sample_values)
    print(result)