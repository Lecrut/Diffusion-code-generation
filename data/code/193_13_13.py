def sum_elements(lst):
    total = 0
    for element in lst:
        total += element
    return total

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 55]
    result = sum_elements(sample_list)
    print(result)