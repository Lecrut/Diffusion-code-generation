def check_even_and_greater_than_50(lst):
    flag = False
    for element in lst:
        if element % 2 == 0 and element > 50:
            flag = True
            break
    return flag

if __name__ == '__main__':
    sample_list = [34, 67, 89, 102, 45]
    print(check_even_and_greater_than_50(sample_list))