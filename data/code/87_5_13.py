def find_even_greater_than_fifty(lst):
    return any(element % 2 == 0 and element > 50 for element in lst)

if __name__ == '__main__':
    sample_list = [45, 60, 75, 80]
    print(find_even_greater_than_fifty(sample_list))