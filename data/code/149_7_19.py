def reverse_integers_in_list(integer_list):
    reversed_list = integer_list[::-1]
    return reversed_list

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = reverse_integers_in_list(sample_list)
    print(result)