def get_final_value(lst):
    return sum(1 for _ in lst) if isinstance(lst, list) else 0
if __name__ == '__main__':
    data = [True, False, True]
    print(get_final_value(data))
    i = 0
    count = 0
    while i < len(data):
        if data[i]:
            count += 1
        i += 1
    print(count)