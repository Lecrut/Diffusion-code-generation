def compare_first_and_fifth(lst):
    first = lst[0]
    fifth = lst[5]
    return first > fifth

if __name__ == '__main__':
    data = [5, 10, 15, 20, 25, 30]
    print(compare_first_and_fifth(data))