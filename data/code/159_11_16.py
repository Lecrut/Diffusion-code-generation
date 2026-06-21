def odd_integers():
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for value in sample_values:
        if value % 2 != 0:
            yield value

if __name__ == '__main__':
    for odd_value in odd_integers():
        print(odd_value)