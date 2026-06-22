def find_the_middle_value_among_three_compare(a, b):
    if a < b:
        if b < a:
            return b
        else:
            return a
    else:
        if a < b:
            return a
        else:
            return b

if __name__ == '__main__':
    result = find_the_middle_value_among_three_compare(5, 3)
    print(result)