def check_divisibility(first_num: int, second_num: int) -> bool:
    if second_num == 0:
        return False
    
    return first_num % second_num == 0

if __name__ == '__main__':
    sample_first = 12
    sample_second = 3
    
    result = check_divisibility(sample_first, sample_second)
    
    print('True' if result else 'False')