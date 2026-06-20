sample_list = [10, 20, 30, 40, 50]

def access_elements(lst):
    positive_index = 2
    negative_index = -1
    return lst[positive_index], lst[negative_index]

if __name__ == '__main__':
    result = access_elements(sample_list)
    print(result)