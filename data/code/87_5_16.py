def check_even_greater_than_fifty(lst):
    found = False
    for value in lst:
        if value % 2 == 0 and value > 50:
            found = True
            break
    return found

if __name__ == '__main__':
    sample_list = [48, 63, 72, 85]
    result = check_even_greater_than_fifty(sample_list)
    print(result)