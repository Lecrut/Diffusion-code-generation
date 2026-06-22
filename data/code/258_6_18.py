def average_pairs(list1, list2):
    if not list1 or not list2:
        return {}
    
    sum_firsts = sum(list1)
    sum_seconds = sum(list2)
    count = len(list1)
    
    return {
        "average_firsts": sum_firsts / count,
        "average_seconds": sum_seconds / count
    }

if __name__ == '__main__':
    sample_list1 = [10, 5, 8, 12]
    sample_list2 = [20, 15, 2, 30]
    result = average_pairs(sample_list1, sample_list2)
    print(result)