TOTAL_LIST = [1, 2, 3, 4, 5]

def sum_total(data_list=TOTAL_LIST):
    return sum(x for x in data_list)

if __name__ == '__main__':
    result = sum_total()
    print(result)