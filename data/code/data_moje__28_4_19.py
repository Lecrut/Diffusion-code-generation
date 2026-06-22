def sort_reverse(a, b):
    result = [a, b]
    result.sort(reverse=True)
    return result

if __name__ == '__main__':
    val1 = 10
    val2 = 5
    print(sort_reverse(val1, val2))