if __name__ == '__main__':
    base_sequence = [1, 2, 3]
    num_repeats = 5
    extended_sequence = (base_sequence * num_repeats)[:len(base_sequence)]
    print(extended_sequence)