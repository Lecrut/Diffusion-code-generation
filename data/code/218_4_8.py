def flatten_and_find_min(nested_list):
    flat_list = [item for sublist in nested_list for item in sublist]
    return min(flat_list)

if __name__ == '__main__':
    data1 = [[5, 2], [8, 1, 9]]
    result1 = flatten_and_find_min(data1)
    print(f"The smallest item in {data1} is: {result1}")

    data2 = [[42, 10], [55, 33]]
    result2 = flatten_and_find_min(data2)
    print(f"The smallest item in {data2} is: {result2}")

    data3 = [[100, 99], [101, 100]]
    result3 = flatten_and_find_min(data3)
    print(f"The smallest item in {data3} is: {result3}")