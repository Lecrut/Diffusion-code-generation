def sort_integers_reverse(a, b):
    return sorted([a, b], reverse=True)

if __name__ == '__main__':
    val1 = 10
    val2 = 25
    result = sort_integers_reverse(val1, val2)
    print(result)