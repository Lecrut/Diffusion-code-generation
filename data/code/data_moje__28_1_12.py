def sort_descending(a, b):
    return sorted([a, b], reverse=True)

if __name__ == '__main__':
    val1 = 10
    val2 = 5
    result = sort_descending(val1, val2)
    print(result)