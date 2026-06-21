def float_exists(lst, num):
    return num in lst

if __name__ == '__main__':
    sample_list = [1.5, 2.3, 4.8, 5.6]
    number_to_check = 3.0
    print(float_exists(sample_list, number_to_check))