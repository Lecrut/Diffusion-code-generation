def reverse_integers_in_list(integer_list):
    return integer_list[::-1]

if __name__ == '__main__':
    sample_list = [123, 456, 789]
    reversed_list = reverse_integers_in_list(sample_list)
    print(reversed_list)