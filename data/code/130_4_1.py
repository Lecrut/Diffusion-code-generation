def check_for_zero(numbers):
    return [number == 0 for number in numbers]
if __name__ == '__main__':
    sample_list = [1, 0, 5, 0, 9, 0]
    result = check_for_zero(sample_list)
    print(result)