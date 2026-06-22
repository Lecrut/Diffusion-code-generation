def sort_three_numbers(a, b, c):
    if not all((isinstance(x, int) for x in [a, b, c])):
        raise ValueError('All inputs must be integers.')
    if a > b:
        temp = a
        a = b
        b = temp
    if a > c:
        temp = a
        a = c
        c = temp
    if b > c:
        temp = b
        b = c
        c = temp
    return (a, b, c)
if __name__ == '__main__':
    sample_values = (5, 1, 3)
    sorted_values = sort_three_numbers(*sample_values)
    print(sorted_values)