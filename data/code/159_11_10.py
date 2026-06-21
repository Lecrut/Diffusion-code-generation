def odd_integers(values):
    for value in values:
        if value % 2 != 0:
            yield value

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9, 11]
    for odd_value in odd_integers(sample_values):
        print(odd_value)