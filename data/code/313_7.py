def contains_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return True
    return False
if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9, 11, 13, 15, 20, 21]
    result = contains_even(sample_list)
    print(result)