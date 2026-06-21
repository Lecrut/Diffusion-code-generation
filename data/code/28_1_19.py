def sort_descending(val1, val2):
    if val1 >= val2:
        return [val1, val2]
    return [val2, val1]

if __name__ == '__main__':
    a = 10
    b = 5
    print(sort_descending(a, b))