def is_valid_element(element):
    return element % 2 == 0 and element > 50

def find_even_greater_than_fifty(lst):
    flag = False
    for element in lst:
        if is_valid_element(element):
            flag = True
            break
    return flag

if __name__ == '__main__':
    sample_list = [45, 60, 75, 80]
    print(find_even_greater_than_fifty(sample_list))