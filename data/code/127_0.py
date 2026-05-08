def has_odd(numbers):
    for number in numbers:
        if number % 2 != 0:
            return True
    return False
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6]
    result = has_odd(sample_list)
    print(result)