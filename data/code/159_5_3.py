def odd_generator(data):
    for num in data:
        if num % 2 != 0:
            yield num
if __name__ == '__main__':
    sample_sequence = range(1, 21)
    odd_numbers = odd_generator(sample_sequence)
    result_list = list(odd_numbers)
    print(result_list)