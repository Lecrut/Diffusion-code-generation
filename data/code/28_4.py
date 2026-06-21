def sort_reverse(a, b):
    result = [a, b]
    result.sort(reverse=True)
    return result

if __name__ == '__main__':
    val1 = 5
    val2 = 10
    print(sort_reverse(val1, val2))