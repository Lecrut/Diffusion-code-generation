def odd_integers(values):
    for value in values:
        if value % 2 != 0:
            yield value

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_gen = odd_integers(sample_values)
    for odd_value in odd_gen:
        print(odd_value)