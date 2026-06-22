sample_values = [True, False, True, False]

def duplicate_list(lst):
    result = lst * 10
    return result

if __name__ == '__main__':
    duplicated_values = duplicate_list(sample_values)
    print(duplicated_values)