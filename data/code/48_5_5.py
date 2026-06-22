import math

def find_largest_data_point(*lists):
    largest_value = -math.inf
    for lst in lists:
        if lst:
            current_max = max(lst)
            if current_max > largest_value:
                largest_value = current_max
    return largest_value

if __name__ == '__main__':
    list1 = [10, 20, 30]
    list2 = [5, 15, 25, 100]
    list3 = [40, 50]
    
    result = find_largest_data_point(list1, list2, list3)
    print(result)