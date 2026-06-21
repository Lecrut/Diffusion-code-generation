from typing import List, Dict

def count_elements(lst: List) -> Dict:
    result = {}
    for item in lst:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 3, 3]
    print(count_elements(sample_list))