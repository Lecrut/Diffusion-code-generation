def odd_generator(data):
    for x in data:
        if x % 2 != 0:
            yield x
if __name__ == '__main__':
    sample_sequence = range(1, 11)
    odd_numbers = odd_generator(sample_sequence)
    result_list = list(odd_numbers)
    print(result_list)