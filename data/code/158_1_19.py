def get_even_numbers(start, end):
    return list(range(start, end + 1))[::2]

if __name__ == '__main__':
    start_num = 5
    end_num = 20
    even_nums = get_even_numbers(start_num, end_num)
    print(even_nums)