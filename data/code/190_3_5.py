def float_exists(lst, num):
    return num in lst

if __name__ == '__main__':
    sample_list = [1.1, 2.2, 3.3, 4.4, 5.5]
    number_to_check = 3.3
    print(float_exists(sample_list, number_to_check))