def is_even_and_greater_than_fifty(element):
    return element % 2 == 0 and element > 50

def find_even_greater_than_fifty(lst):
    if not lst:
        raise ValueError("List cannot be empty")
    flag = any(is_even_and_greater_than_fifty(element) for element in lst)
    return flag

if __name__ == '__main__':
    sample_list = [45, 60, 75, 80]
    print(find_even_greater_than_fifty(sample_list))