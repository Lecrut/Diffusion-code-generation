def count_even_numbers(lst):
    count = 0
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            count += 1
        i += 1
    return count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6]
    print(count_even_numbers(sample_list))