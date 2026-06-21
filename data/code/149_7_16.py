def reverse_integers_list(int_list):
    return int_list[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_integers_list(sample_list)
    print(reversed_list)