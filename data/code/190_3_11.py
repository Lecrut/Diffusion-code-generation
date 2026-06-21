def float_exists(lst, num):
    return num in lst

if __name__ == '__main__':
    sample_list = [1.5, 2.3, 3.7, 4.1]
    number_to_check = 3.7
    print(float_exists(sample_list, number_to_check))