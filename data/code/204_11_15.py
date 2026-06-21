def binary_search_median(data):
    n = len(data)
    if n == 0:
        return None

    def partition(left, right, pivot_index):
        pivot_value = data[pivot_index]
        data[pivot_index], data[right] = data[right], data[pivot_index]
        store_index = left
        for i in range(left, right):
            if data[i] < pivot_value:
                data[store_index], data[i] = data[i], data[store_index]
                store_index += 1
        data[right], data[store_index] = data[store_index], data[right]
        return store_index

    left, right = 0, n - 1
    while True:
        pivot_index = random.randint(left, right)
        new_pivot_index = partition(left, right, pivot_index)

        if new_pivot_index == n // 2:
            if n % 2 == 1:
                return data[new_pivot_index]
            else:
                return (data[new_pivot_index] + data[new_pivot_index - 1]) / 2.0
        elif new_pivot_index < n // 2:
            left = new_pivot_index + 1
        else:
            right = new_pivot_index - 1

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    print(binary_search_median(list1))
    list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(binary_search_median(list2))