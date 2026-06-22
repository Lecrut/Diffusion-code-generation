def sort_descending(a, b):
    if a > b:
        return (a, b)
    else:
        return (b, a)

if __name__ == '__main__':
    result = sort_descending(3.5, 7.2)
    print(result)