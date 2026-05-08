def recursive_sum(data):
    if not data:
        return 0
    else:
        return data[0] + recursive_sum(data[1:])
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = recursive_sum(sample_list)
    print(result)