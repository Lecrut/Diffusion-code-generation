def max_absolute_difference(list_a, list_b):
    if not list_a or not list_b:
        return 0
    min_a = min(list_a)
    max_a = max(list_a)
    min_b = min(list_b)
    max_b = max(list_b)
    return max(abs(max_a - min_b), abs(max_b - min_a))

if __name__ == '__main__':
    list_a = [10, 20, 30]
    list_b = [5, 15, 25]
    print(max_absolute_difference(list_a, list_b))