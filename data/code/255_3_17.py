def find_max_sum_tuple(tuple_list):
    if not tuple_list:
        return None
    return max(tuple_list, key=sum)

if __name__ == '__main__':
    sample_data = [(10, 5, 22), (30, 15, 40), (1, 50, 3)]
    result = find_max_sum_tuple(sample_data)
    print(result)