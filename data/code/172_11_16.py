def map_numbers_to_words(numbers):
    mapping = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    return {num: mapping[num] for num in numbers if num in mapping}

if __name__ == '__main__':
    sample_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(map_numbers_to_words(sample_numbers))