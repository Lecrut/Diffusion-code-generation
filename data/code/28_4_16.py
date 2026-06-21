def sort_reverse(a, b):
    return sorted([a, b], reverse=True)

if __name__ == '__main__':
    val_a = 42
    val_b = 17
    result = sort_reverse(val_a, val_b)
    print(result)