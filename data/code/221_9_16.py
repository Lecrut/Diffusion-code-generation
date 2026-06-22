def validate_inputs(a, b, c):
    if not all((isinstance(x, int) for x in [a, b, c])):
        raise ValueError('All inputs must be integers')

def sort_three_numbers(a, b, c):
    validate_inputs(a, b, c)
    if a > b:
        temp = a
        a = b
        b = temp
    if b > c:
        temp = b
        b = c
        c = temp
    return (a, b, c)
if __name__ == '__main__':
    sorted_numbers = sort_three_numbers(3, 1, 2)
    print(sorted_numbers)