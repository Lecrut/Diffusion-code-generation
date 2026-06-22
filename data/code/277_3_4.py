def count_even_numbers(lst):
    count = 0
    index = 0
    while index < len(lst):
        if lst[index] % 2 == 0:
            count += 1
        index += 1
    return count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6]
    print(count_even_numbers(sample_list))