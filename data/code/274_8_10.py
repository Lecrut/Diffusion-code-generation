sample_list = [1, 2, 3, 4, 5]
condition_value = 3

def print_until_condition(lst, condition):
    index = 0
    while index < len(lst) and lst[index] != condition:
        print(lst[index])
        index += 1

if __name__ == '__main__':
    print_until_condition(sample_list, condition_value)