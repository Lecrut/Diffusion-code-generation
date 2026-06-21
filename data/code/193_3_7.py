def sum_elements(lst):
    return sum(lst) if lst else 0
if __name__ == '__main__':
    print(sum_elements([1, 2, 3]))
    print(sum_elements([]))