def check_integers(numbers, flag):
    result = []
    for num in numbers:
        if flag:
            if num % 2 == 0:
                result.append(True)
            else:
                result.append(False)
        else:
            result.append(False)
    return result
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    sample_flag_true = True
    sample_flag_false = False
    result_true = check_integers(sample_numbers, sample_flag_true)
    print(f"Numbers: {sample_numbers}, Flag: {sample_flag_true}")
    print(f"Result: {result_true}")
    result_false = check_integers(sample_numbers, sample_flag_false)
    print(f"Numbers: {sample_numbers}, Flag: {sample_flag_false}")
    print(f"Result: {result_false}")