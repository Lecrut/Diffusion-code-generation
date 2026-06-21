def odd_integers(values):
    for value in values:
        if value % 2 != 0:
            yield value

if __name__ == '__main__':
    sample_values = [11, 13, 15, 17, 19, 20, 22]
    for odd_value in odd_integers(sample_values):
        print(odd_value)