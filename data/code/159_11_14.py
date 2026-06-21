def is_odd(value):
    return value % 2 != 0

def odd_integers(values):
    for value in values:
        if is_odd(value):
            yield value

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9, 10]
    odd_gen = odd_integers(sample_values)
    for odd_value in odd_gen:
        print(odd_value)