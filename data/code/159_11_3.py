def odd_integers(values):
    for value in values:
        if value % 2 != 0:
            yield value

if __name__ == '__main__':
    sample_values = [11, 13, 15, 17, 19, 20, 22]
    odd_gen = odd_integers(sample_values)
    
    for odd_value in odd_gen:
        print(odd_value)