EVEN_THRESHOLD = 50

def check_even_greater_than_threshold(lst):
    flag = False
    for element in lst:
        if element % 2 == 0 and element > EVEN_THRESHOLD:
            flag = True
    return flag

if __name__ == '__main__':
    sample_list = [45, 60, 75, 80]
    print(check_even_greater_than_threshold(sample_list))