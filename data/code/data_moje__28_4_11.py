def sort_reverse(a, b):
    lst = [a, b]
    lst.sort(reverse=True)
    return lst

if __name__ == '__main__':
    result = sort_reverse(42, 17)
    print(result)