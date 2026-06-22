def find_the_middle_value_among_three_batch_process(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_batch_process(1, 5, 3))
    print(find_the_middle_value_among_three_batch_process(10, 20, 5))
    print(find_the_middle_value_among_three_batch_process(7, 1, 9))
    print(find_the_middle_value_among_three_batch_process(4, 8, 2))
    print(find_the_middle_value_among_three_batch_process(100, 50, 25))