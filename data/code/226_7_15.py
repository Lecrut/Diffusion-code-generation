sample_values = [True, False, True, True, False]

def duplicate_list(lst):
    result = lst[:]
    for _ in range(9):
        result += lst
    return result

if __name__ == '__main__':
    print(duplicate_list(sample_values))