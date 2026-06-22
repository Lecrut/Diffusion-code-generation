def check_even(n):
    even_list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_list

if __name__ == '__main__':
    sample_values = [4, 7, 10, 13, 20]
    results = [check_even(val) for val in sample_values]
    print(results)