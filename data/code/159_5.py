def odd_number_generator(data):
    for num in data:
        if num % 2 != 0:
            yield num
if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_gen = odd_number_generator(sample_sequence)
    result_list = list(odd_gen)
    print(result_list)