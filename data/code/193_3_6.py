def sum_elements(lst):
    if not lst:
        return 0
    return sum(lst)

if __name__ == '__main__':
    print(sum_elements([1, 2, 3]))
    print(sum_elements([]))