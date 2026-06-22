def find_the_middle_value_among_three_compare(a, b):
    if a < b:
        return b
    else:
        return a

if __name__ == '__main__':
    result = find_the_middle_value_among_three_compare(5, 3)
    print(result)